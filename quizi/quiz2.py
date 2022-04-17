import os
import boto3

def download_file(client, file_name: str, bucket_name: str, output: str)-> bool:
    client.meta.client.download_file(bucket_name, file_name, output)

def upload_file(client, file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

        print(file_name)

        client.upload_file(file_name, bucket, object_name)
    return True

def main():
    s3_client = boto3.clinet("s3")

    download_file(s3_client, "my_file.txt", "my-a-bucket")
    upload_file(s3_client, "my_file.txt", "my-b-bucket")
