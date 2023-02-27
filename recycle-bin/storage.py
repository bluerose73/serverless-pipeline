import io
import os
import uuid

import boto3
import json
import oss2

class storage:
    def get_instance():
        with open('config.json') as f:
            config = json.load(f)["storage"]
        provider = config["provider"]
        args = config["args"][provider]

        if provider == "AWS":
            return AWS_storage.get_instance(**args)
        elif provider == "aliyun":
            return aliyun_storage.get_instance(**args)
        else:
            raise NotImplementedError

class AWS_storage:
    instance = None
    client = None

    def __init__(self, access_key_id, access_key_secret):
        self.client = boto3.client(
            's3',
            aws_access_key_id = access_key_id,
            aws_secret_access_key = access_key_secret
        )

    @staticmethod
    def unique_name(name):
        name, extension = os.path.splitext(name)
        return '{name}.{random}.{extension}'.format(
                    name=name,
                    extension=extension,
                    random=str(uuid.uuid4()).split('-')[0]
                )
    
    def upload(self, bucket, file, filepath):
        key_name = AWS_storage.unique_name(file)
        self.client.upload_file(filepath, bucket, key_name)
        return key_name
    
    def download(self, bucket, file, filepath):
        self.client.download_file(bucket, file, filepath)

    def download_directory(self, bucket, prefix, path):
        objects = self.client.list_objects_v2(Bucket=bucket, Prefix=prefix)
        for obj in objects['Contents']:
            file_name = obj['Key']
            path_to_file = os.path.dirname(file_name)
            os.makedirs(os.path.join(path, path_to_file), exist_ok=True)
            self.download(bucket, file_name, os.path.join(path, file_name))

    def upload_stream(self, bucket, file, data):
        key_name = AWS_storage.unique_name(file)
        self.client.upload_fileobj(data, bucket, key_name)
        return key_name

    def download_stream(self, bucket, file):
        data = io.BytesIO()
        self.client.download_fileobj(bucket, file, data)
        return data.getbuffer()
    
    def get_instance(access_key_id, access_key_secret):
        if AWS_storage.instance is None:
            AWS_storage.instance = AWS_storage(access_key_id, access_key_secret)
        return AWS_storage.instance


class aliyun_storage:
    instance = None
    client = None

    def __init__(self, access_key_id, access_key_secret, endpoint):
        self.auth = oss2.Auth(access_key_id, access_key_secret)
        self.endpoint = endpoint

    @staticmethod
    def unique_name(name):
        name, extension = os.path.splitext(name)
        return '{name}.{random}.{extension}'.format(
                    name=name,
                    extension=extension,
                    random=str(uuid.uuid4()).split('-')[0]
                )
    
    def upload(self, bucket, file, filepath):
        key_name = aliyun_storage.unique_name(file)
        bucket = oss2.Bucket(self.auth, self.endpoint, bucket)
        bucket.put_object_from_file(key_name, filepath)
        return key_name
    
    def download(self, bucket, file, filepath):
        bucket = oss2.Bucket(self.auth, self.endpoint, bucket)
        bucket.get_object_to_file(file, filepath)

    def download_directory(self, bucket, prefix, path):
        # objects = self.client.list_objects_v2(Bucket=bucket, Prefix=prefix)
        # for obj in objects['Contents']:
        #     file_name = obj['Key']
        #     path_to_file = os.path.dirname(file_name)
        #     os.makedirs(os.path.join(path, path_to_file), exist_ok=True)
        #     self.download(bucket, file_name, os.path.join(path, file_name))
        bucket = oss2.Bucket(self.auth, self.endpoint, bucket)
        for obj in oss2.ObjectIteratorV2(bucket, prefix=prefix):
            file_name = obj.key
            path_to_file = os.path.dirname(file_name)
            os.makedirs(os.path.join(path, path_to_file), exist_ok=True)
            self.download(bucket, file_name, os.path.join(path, file_name))

    def upload_stream(self, bucket, file, data):
        key_name = aliyun_storage.unique_name(file)
        bucket = oss2.Bucket(self.auth, self.endpoint, bucket)
        bucket.put_object(key_name, data)
        return key_name

    def download_stream(self, bucket, file):
        # WARNING: need test
        # 
        # data = io.BytesIO()
        # self.client.download_fileobj(bucket, file, data)
        # return data.getbuffer()
        bucket = oss2.Bucket(self.auth, self.endpoint, bucket)
        result = bucket.get_object(file)
        return result.read()
    
    def get_instance(access_key_id, access_key_secret, endpoint):
        if aliyun_storage.instance is None:
            aliyun_storage.instance = aliyun_storage(access_key_id, access_key_secret, endpoint)
        return aliyun_storage.instance
