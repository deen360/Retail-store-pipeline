import os
import logging

from datetime import datetime


from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from google.cloud import storage
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator
import pyarrow.csv as pv
import pyarrow.parquet as pq



# Helps to interact with Google Storage
from google.cloud import storage

#project and bucket id
PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")



#path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

#gets or create all_online_retail if none exists
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", 'all_online_retail')

#function that converts csv file to parquet
def format_to_parquet(src_file):
    print(src_file)
    if not src_file.endswith('.csv'):
        logging.error("Can only accept source files in CSV format or .csv.zip, for the moment")
        return
    table = pv.read_csv(src_file)
    pq.write_table(table, src_file.replace('.csv', '.parquet')) 


# NOTE: takes 20 mins, at an upload speed of 800kbps. Faster if your internet has a better upload speed
def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    :param bucket: GCS bucket name
    :param object_name: target path & file-name
    :param local_file: source path & file-name
    :return:
    """
    # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # (Ref: https://github.com/googleapis/python-storage/issues/74)
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB
    # End of Workaround

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)




default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 3,
}





URL_PREFIX = 'kaggle datasets download -d'



#this can be changed to any kaggle dataset you are interested in, you just have to copy the uploader name and file name
#MODIFY DATASET_ID, DATA_NAME, FILE_NAME to desired dataset, and do the same in the script.sh file

DATASET_ID = "mashlyn"

DATA_NAME="online-retail-ii-uci"

FILE_NAME = "online_retail_II.csv"


URL_SUFFIX = DATASET_ID + "/" + DATA_NAME


FILE_NAME_TO_PARQUET = FILE_NAME.replace(".csv",".parquet")

URL_TEMPLATE = AIRFLOW_HOME + DATASET_ID + "/" + FILE_NAME


PARQUET_TEMPLATE = AIRFLOW_HOME + "/" + DATASET_ID + "/" + FILE_NAME_TO_PARQUET


GCS_PATH_TEMPLATE = f"kaggle/{DATASET_ID}/{FILE_NAME_TO_PARQUET}"


# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="data_ingestion_gcs_project_dag-12",
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['dtc-deen'],
) as dag:

    download_dataset_task = BashOperator(
        task_id="download_dataset_task",
        bash_command= "script.sh"
    )



    format_to_parquet_task = PythonOperator(
        task_id="format_to_parquet_task",
        python_callable=format_to_parquet,
        op_kwargs={
        "src_file": f"{AIRFLOW_HOME}/{DATASET_ID}/{FILE_NAME}"

        },
    )

    local_to_gcs_task = PythonOperator(
        task_id="local_to_gcs_task",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": GCS_PATH_TEMPLATE,
            "local_file": PARQUET_TEMPLATE,
        },
    )

    
    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id="bigquery_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": f"{DATA_NAME}_external_table",
            },
            "externalDataConfiguration": {
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET}/kaggle/{DATASET_ID}/{FILE_NAME_TO_PARQUET}"],
            },
        },
    )

    
    download_dataset_task  >> format_to_parquet_task >> local_to_gcs_task >> bigquery_external_table_task
