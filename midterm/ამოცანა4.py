import boto3
import argparse

s3 = boto3.client('s3')

def file_operations(bucket_name,file_name,operation):
    if (operation =="download"):
        download_file(bucket_name,file_name)
    else:
        delete_file(bucket_name,file_name)

def delete_file(bucket_name,file_name):
    if(key_exists(bucket_name,file_name)):
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        print('file was succesfully deleted')
    else:
        print("File doesnt exists")

def download_file(bucket_name,file_name):
    save_path='./'+file_name

    if(key_exists(bucket_name,file_name)):
        s3.download_file(bucket_name,file_name,save_path)
        print('file was succesfully downloaded')
    else:
        print("File doesnt exists")

def key_exists(bucket_name, file_name):
    result = s3.list_objects(Bucket=bucket_name)
    for obj in result.get("Contents", []):
        if(obj.get("Key") == file_name):
            return True
        return False

def main():
    file_operations("users123","1.txt","delete")

if __name__ == "__main__":
    main()

