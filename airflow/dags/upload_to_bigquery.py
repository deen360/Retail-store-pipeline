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

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")



#path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

#dataset_file = dataset_file.replace('.parquet', '.csv')

#parquet_file = dataset_file.replace('.csv', '.parquet')
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", 'all_online_retail')



#here we convertthe file to from csv to parquet or from csv.zip to csv to parquet, this depends on if the file is zipped or not then it removes the zip file and only keeps the csv file   

#/re-write





# NOTE: takes 20 mins, at an upload speed of 800kbps. Faster if your internet has a better upload speed



default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 3,
}



DATA_NAME="online-retail"



# NOTE: DAG declaration - using a Context Manager (an implicit way)

with DAG(
    dag_id="data_ingestion_gcs_project_dag-14",
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['dtc-deen'],
) as dag:


    #to be checked 
    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id="bigquery_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": f"{DATA_NAME}_cleaned",
            },
            "externalDataConfiguration": {
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET}/kaggle_cleaned/online_retail_cleaned/*.parquet"],
            },
        },
    )

    
bigquery_external_table_task
