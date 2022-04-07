import boto3
import argparse

s3 = boto3.client('s3')

def put_file(bucket_name,file_name):
        with open(file_name, "rb") as file:
            s3.put_object(Bucket=bucket_name, Key=file_name, Body=file.read())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bucket_name')
    parser.add_argument('-f', '--file_name')
    parsed = parser.parse_args()
    put_file(parsed.bucket_name,parsed.file_name)

if __name__ == "__main__":
    main()

# exec :   python .\davaleba3\davaleba3_1.py -b prodmybucketwiko -f davaleba3/test.html
# C:\Users\Gio\PycharmProjects\pythonProject\davaleba3\test an davaleba3/test