import boto3
import os 

class S3Handler:

    def __init__(self, bucket_name):

        self.s3=boto3.client("s3")
        self.bucket_name = bucket_name

        def upload_file(self, file_path, s3_key):
            try:
                self.s3.upload_file(file_path, self.bucket_name, s3_key)
                print(f"Uploaded {file_path} to s3://{self.bucket_name}/{s3_key}")
                return f"s3://{self.bucket_name}/{s3_key}"
        
            except Exception as e:
                print(f"Error uploading file: {e}")
                return None
