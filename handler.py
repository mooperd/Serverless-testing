import json
import requests
import pandas
import arrow
import base64
import os




def run(event, context):
    print(os.environ['S3_BUCKET'])
    print(os.environ['S3_KEY_BASE'])
    url = "https://cache1.phantombooster.com/ukZxdjCQmz0/Vg7zuvUGSEG6yzglJ6jkhA/result.json"
    df = pandas.read_json(requests.get(url).text)
    random_string = base64.b64encode(arrow.utcnow().format('SSSSSSSSS').encode('ascii')).decode("utf-8")
    df.to_csv("s3://{}/{}/{}.csv".format(os.environ['S3_BUCKET'], os.environ['S3_KEY_BASE'], random_string))


