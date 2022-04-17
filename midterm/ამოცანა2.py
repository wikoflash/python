import boto3

s3 = boto3.client('s3')

def print_files():
    result = s3.list_objects(Bucket="prodmybucketwiko")
    key_list = result.get("Contents", [])
    key_list_sorted = sorted(key_list, key=lambda x: x["Key"])

    for obj in key_list_sorted:
        print(obj.get("Key"))

def main():
    print_files()

if __name__ == "__main__":
    main()
