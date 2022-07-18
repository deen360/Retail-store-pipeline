he Data Engineeing project 

introduction 
the aim of this project is the design data pipeline for a dataset from from the data source to the datalake and  to create a pipeline for moving the data from the datalake to a data warehouse then finally to create a dashboard.

Technologies Used 

Dataset source 
Kaggle api(for Kaggle dataset): https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci


Cloud services: Google Cloud Platform

Infrastructure as code: Terraform 

Workflow orchestration: Airflow

Data warehouse: Bigquery

Data Transformation: Spark (using Jupyter Notebook)

Dashboard: data studio

Overview
the sequence of steps used in this project is shown the image below 

###########image################""
he Data Engineeing project 

introduction 
the aim of this project is the design data pipeline for a dataset from from the data source to the datalake and  to create a pipeline for moving the data from the datalake to a data warehouse then finally to create a dashboard.

Technologies Used 

Dataset source 
Kaggle api(for Kaggle dataset): https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci


Cloud services: Google Cloud Platform

Infrastructure as code: Terraform 

Workflow orchestration: Airflow

Data warehouse: Bigquery

Data Transformation: Spark (using Jupyter Notebook)

Dashboard: data studio

Overview
the sequence of steps used in this project is shown the image below 


/images/Screenshot from 2022-07-16 23-37-25.png

Explanation,
data was downloaded from the kaggle website using the kaggle api and the private keys generated from the kaggle website,the api command and the export keys were written in a bash script (script.sh). and was executed with airflow as task using the bash operator. in the script.sh the file was downloaded to local and unwrapped, the python operator was used to convert the file from a csv to a parquet format, after which it was the uploaded into a storage bucket, google cloud storage., a copy was also uploaded to the bigquery, to get a brief insight to see if the data needs cleansing or modification. from the the data was downloaded into a notebook, where various cleaning and modificatiosn were done using pandas and pyspark, an additional column was added(Total), after the various modifications were made, the clean data was seng into the bucket ( making us have both the raw uncleaded data and the cleaned data),airflow was used to transfer the cleaned data to big query and finally to datastudio for the dashboard to be made.


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



Explanation,
data was downloaded from the kaggle website using the kaggle api and the private keys generated from the kaggle website,the api command and the export keys were written in a bash script (script.sh). and was executed with airflow as task using the bash operator. in the script.sh the file was downloaded to local and unwrapped, the python operator was used to convert the file from a csv to a parquet format, after which it was the uploaded into a storage bucket, google cloud storage., a copy was also uploaded to the bigquery, to get a brief insight to see if the data needs cleansing or modification. from the the data was downloaded into a notebook, where various cleaning and modificatiosn were done using pandas and pyspark, an additional column was added(Total), after the various modifications were made, the clean data was seng into the bucket ( making us have both the raw uncleaded data and the cleaned data),airflow was used to transfer the cleaned data to big query and finally to datastudio for the dashboard to be made.


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

