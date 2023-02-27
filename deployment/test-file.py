import boto3
import json

with open('test-s3-config.json') as config_file:
    config = json.load(config_file)

bucketname = config['bucket']

client = boto3.client(
    service_name = 's3',
    endpoint_url = config['endpoint'],
    aws_access_key_id = config['access_key_id'],
    aws_secret_access_key = config['access_key_secret']
)

client.create_bucket(Bucket = bucketname)

client.upload_file('test-s3.py', bucketname, 'test-file.py')
client.download_file(bucketname, 'test-file.py', 'test-file.py')

print('test finished.')