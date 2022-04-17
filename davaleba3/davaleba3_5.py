import boto3
import argparse
import pprint

s3 = boto3.client('s3')

def check_versioning(bucket_name):
    s3_res = boto3.resource('s3')
    versioning = s3_res.BucketVersioning(bucket_name)

    if(versioning.status == 'Enabled'):
        print(versioning.status)
    else:
        enable_versioning(bucket_name)

def enable_versioning(bucket_name):
   response = s3.put_bucket_versioning(
       Bucket=bucket_name,
       VersioningConfiguration={
           "Status": "Enabled",
       },
   )

def getasd(bucket_name,file_name):
    versions =s3.list_object_versions(Bucket = bucket_name)

    #for version in versions.get("Contents", []):

    pprint.pprint(versions)
    # for version in versions:
    #    version
    #pprint.print(k.version_id for k in versions)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bucket_name')
    parser.add_argument('-f', '--file_name')
    parsed = parser.parse_args()
    #check_versioning(parsed.bucket_name)
    getasd(parsed.bucket_name,parsed.file_name)


if __name__ == "__main__":
    main()
