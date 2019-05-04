import boto3
import os


class S3Manipurator():
    def __init__(self, bucket_name=None, aws_access_key_id=None, aws_secret_access_key=None):

        if bucket_name is not None:
            self.bucket_name = bucket_name
        else:
            self.bucket_name = os.getenv('BUCKET_NAME')

    
        if aws_access_key_id is not None:
            self.aws_access_key_id = aws_access_key_id
        else:
            self.aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        
        if aws_secret_access_key is not None:
            self.aws_secret_access_key = aws_secret_access_key
        else:
            self.aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

        self.client = boto3.resource('s3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key) 
    
    def upload(self, filepath):
        filename = os.path.basename(filepath)
        self.client.Bucket(self.bucket_name).upload_file(filepath, filename)

