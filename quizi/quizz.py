import boto3

s3_client = boto3.client('s3')

def delete_file(bucket_name):
    response = s3_client.list_buckets()

    for buck in response['Buckets']:
        if buck["Name"] == bucket_name:
            result = s3_client.list_objects(Bucket=buck["Name"])
            for obj in result.get("Contents", []):
                s3_client.delete_object(Bucket=bucket_name, Key=obj.get("Key"))

def main():
    bucket_name = ('testbucket')
    delete_file(bucket_name)

if __name__ == "__main__":
    main()
