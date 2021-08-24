import boto3
import os

def download_files_from_s3bucket():

    #read key and secret from Jenkins credentials store
    key=os.environ['AWS_KEY']
    secret=os.environ['AWS_SECRET']
    
    BUCKET_NAME = 'hpt-first-bucket' 
    KEY = 'artifacts/home.png'
    
    s3 = boto3.client('s3', aws_access_key_id=key,aws_secret_access_key=secret)
    s3.download_file('hpt-first-bucket','artifacts/home.png','k.png')

download_files_from_s3bucket()
