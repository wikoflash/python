import boto3

s3 = boto3.client('s3')

def print_my_bucket_by_name_users():
    response = s3.list_buckets()

    print('List of buckets:')
    for buck in response['Buckets']:
        if buck["Name"].startswith('users'):
            print(f'{buck["Name"]}')

def main():
    print_my_bucket_by_name_users()

if __name__ == "__main__":
    main()