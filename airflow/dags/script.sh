#!/usr/bin
pip install kaggle

export KAGGLE_USERNAME=yuxxxxxxxxxxxxxxxxx
export KAGGLE_KEY=f9e7d64641f620xxxxxxxxxxxxxx




DATASET_ID=mashlyn
DATASET_NAME=online-retail-ii-uci

kaggle datasets download -d $DATASET_ID/$DATASET_NAME --unzip -p "/opt/airflow/$DATASET_ID"






