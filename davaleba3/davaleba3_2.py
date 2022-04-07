import boto3
import argparse

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def delete_file(bucket_name,file_name):
    if(key_exists(bucket_name,file_name)):
        s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        print('file was succesfully deleted')
    else:
        print("File Doesnt exists")

#def key_exists(bucket_name, file_name):
#    bucket = s3.Bucket(bucket_name)
#    file_name = file_name
#    obj = list(bucket.objects.filter(Prefix=file_name))
#   if len(obj) > 0:
#       print("File exists")
#        return True
#    else:
#        print("File Doesnt exists")
#        return False

def key_exists(bucket_name, file_name):
    obj = s3_resource.Object(bucket_name, file_name)
    try:
        obj.load()
        return True
    except:
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bucket_name')
    parser.add_argument('-f', '--file_name')
    parsed = parser.parse_args()
    delete_file(parsed.bucket_name,parsed.file_name)

if __name__ == "__main__":
    main()

# exec :   python .\davaleba3\davaleba3_2.py -b prodmybucketwiko -f davaleba3/test.html