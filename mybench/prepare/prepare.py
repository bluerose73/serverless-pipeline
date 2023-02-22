import boto3, json, os
from input import generate_input

def upload_files(data_root, data_dir, bucket):

    for root, dirs, files in os.walk(data_dir):
        prefix = os.path.relpath(root, data_root).replace('\\', '/')
        for file in files:
            file_name = prefix + '/' + file
            filepath = os.path.join(root, file)
            bucket.upload_file(Filename=filepath, Key=file_name)

if __name__ == '__main__':
    s3 = boto3.resource('s3')
    with open('../meta-config.json') as f:
        metaconf = json.load(f)
    benchmarks = metaconf["benchmarks"]
    upload_bucket = s3.Bucket(metaconf['bucket']['input'])

    print('Uploading files...')
    upload_files('./data', './data', upload_bucket)
