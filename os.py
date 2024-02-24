import boto3
import elasticsearch
from elasticsearch import Elasticsearch, RequestsHttpConnection
from aws_requests_auth.aws_auth import AWSRequestsAuth

sts_client = boto3.client('sts')
assumed_role_object = sts_client.assume_role( RoleArn="",RoleSessionName="test-session",DurationSeconds=3600 )
credentials=assumed_role_object['Credentials']
es_host = 'aa'
session = boto3.session.Session()

credentials = assumed_role_object["Credentials"]


awsauth = AWSRequestsAuth(
    aws_access_key=credentials["AccessKeyId"],
    aws_secret_access_key=credentials["SecretAccessKey"],
    aws_token=credentials["SessionToken"],
    aws_host=es_host,
    aws_region='us-east-1',
    aws_service='es'
)
es = elasticsearch.Elasticsearch(
    hosts=[{'host': es_host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=elasticsearch.RequestsHttpConnection
)


response = es.index(index = "sample", id = "helloo" , body =  body )
print(response)
