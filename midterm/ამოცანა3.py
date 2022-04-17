import boto3

s3 = boto3.client('s3')

def print_my_bucket_by_name(bucket_name):
    response = s3.list_buckets()
    bucket_exists = False

    for buck in response['Buckets']:
        if buck["Name"] == bucket_name:
            bucket_exists = True
            print(f'bucket with name {bucket_name} already exists')

    if not bucket_exists == True:
            bucket_create_by_name(bucket_name)

def bucket_create_by_name(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} was created successfully")
    except Exception as ex:
        print(ex)

def main():
    print_my_bucket_by_name("users123")

if __name__ == "__main__":
    main()
