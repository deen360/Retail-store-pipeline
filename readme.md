The Data Engineeing project 

Introduction
  The aim of this project is the design a data pipeline for moving a dataset from the data source to the datalake and to create a pipeline for moving the data from the datalake to a data warehouse and then finally to create a dashboard.

Technologies Used 
Dataset source 
![kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)
api(for Kaggle dataset)

Cloud services: Google Cloud Platform

Infrastructure as code: Terraform 

Workflow orchestration: Airflow

Data warehouse: Bigquery

Data Cleaning: pySpark (using Jupyter Notebook)

Dashboard: data studio

Overview
  The sequence of steps used in this project are shown in the image below 
![Screenshot from 2022-07-16 23-37-25](https://user-images.githubusercontent.com/74934494/179567939-74a122e6-df54-4323-940d-d0eb300ff1ee.png)


Explanation,
Data was downloaded from the kaggle website using the kaggle api and the private keys generated from the kaggle website,the api command and the export keys were written in a bash script (script.sh). which was executed with airflow as task using the bash operator. in the script.sh the file was downloaded to local and unwrapped, the python operator was used to convert the file from a csv to a parquet format, after which it was the uploaded into a storage bucket, google cloud storage, a copy was also uploaded to the bigquery, to get a brief insight to see if the data needs cleansing or modifications. from there the data was downloaded into a notebook, where various cleaning and modificatiosn were done using pandas and pyspark, an additional column was added (Total), after the various modifications were made, the clean data was sent into the bucket (making us have both the raw uncleaded data and the cleaned data),airflow was used to transfer the cleaned data to big query and finally the bigquery was connected to datastudio for the dashboard to be created.


Cloud services: Google Cloud Platform
- sotarage bucket 

Infrastructure as code: Terraform 
-set up infastructure  for bucket(data lake) and bigquery(data warehouse)


Workflow orchestration: Airflow
download data to local
convert to parquet
upload to google cloud storage 
upload to big query 

Data warehouse: Bigquery
used as data ware house 
used to connect data to data studio

Data Transformation: Spark (using Jupyter Notebook)
used to clean data
to add custom columns and fuctions


Dashboard: data studio
used to create dashboard 

#dashboard link 
![datastudio](https://datastudio.google.com/reporting/a713b799-202f-40ed-80b8-e1002ff5bf47)

![Screenshot from 2022-07-17 09-43-16](https://user-images.githubusercontent.com/74934494/179569709-abd7c1ee-c01d-4de5-aea5-923d2af0bbc5.png)


