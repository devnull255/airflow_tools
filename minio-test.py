#!/usr/bin/env/python
import argparse
import boto3
import os
from botocore.client import Config

endpoint_url = os.environ['endpoint_url']
aws_access_key_id = os.environ['aws_access_key_id']
aws_secret_access_key = os.environ['aws_secret_access_key']
user_dir = os.environ['USERPROFILE']

print(f"endpoint: {endpoint_url}")
print(f"user_dir: {user_dir}")

s3 = boto3.resource('s3',
                    endpoint_url=endpoint_url,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

s3.Bucket('airflow-dags').download_file('hello_minio_dag.py', user_dir + '/Downloads/hello_minio_dag.py')
