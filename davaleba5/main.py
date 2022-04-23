import pprint
import time
import boto3

s3 = boto3.client("s3")
lambda_client = boto3.client('lambda')
ZIPNAME = "lambda_function.zip"
bucket_name = "wikotest2"
lambda_name = "lambda5"
file_name = "airosft.jpg"

def create_bucket(bucket_name):
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

def aws_file():
    with open(ZIPNAME, 'rb') as file_data:
        bytes_content = file_data.read()
    return bytes_content

def create_lambda(lambda_name):
    response = lambda_client.create_function(
        Code={
            'ZipFile': aws_file()
        },
        Description='Recognize object from photos',
        FunctionName=lambda_name,
        Handler='lambda_function.lambda_handler',
        Publish=True,
        Role='arn:aws:iam::607371281461:role/LabRole',
        Runtime='python3.8',
    )
    return response

def add_permission(bucket_name, lambda_name):
    lambda_client.add_permission(
        FunctionName=lambda_name,
        StatementId='AllowToBeInvoked',
        Action='lambda:InvokeFunction',
        Principal='s3.amazonaws.com',
        SourceArn=f'arn:aws:s3:::{bucket_name}',
    )

def get_lambda_arn(function_name):
    return lambda_client.get_function(FunctionName=function_name)['Configuration'][
        'FunctionArn'
    ]

def s3_trigger(bucket_name, lambda_name):
    #print(get_lambda_arn(lambda_name))
    add_permission(bucket_name, lambda_name)
    response = s3.put_bucket_notification_configuration(
        Bucket=bucket_name,
        NotificationConfiguration={'LambdaFunctionConfigurations': [
            {
                'LambdaFunctionArn':get_lambda_arn(lambda_name),
                'Events': [
                    's3:ObjectCreated:*'
                ],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name':  'suffix',
                                'Value': '.jpg'
                            },
                        ]
                    }
                }
            },
        ],
          },
        SkipDestinationValidation = True
    )
    return response

def upload_file(file_name, bucket_name):
    try:
        s3.upload_file(file_name, bucket_name, file_name)
    except Exception as ex:
        print(ex)

def check_json(file_name, bucket_name):
    try:
        data = s3.get_object(Bucket=bucket_name, Key=file_name.replace('.jpg', '.json'))
        contents = data['Body'].read()
        print(contents)
    except Exception as ex:
        print(ex)

def main():
    create_bucket(bucket_name)
    create_lambda(lambda_name)
    s3_trigger(bucket_name, lambda_name)
    upload_file(file_name, bucket_name)

    check_json(file_name, bucket_name)

    #respone = s3_trigger(bucket_name, lambda_name)
    #pprint.pprint(respone)



if __name__ == '__main__':
    main()