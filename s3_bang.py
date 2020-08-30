import pandas
import requests
import arrow
import base64
import os

def s3_bang():
    url = "https://cache1.phantombooster.com/ukZxdjCQmz0/Vg7zuvUGSEG6yzglJ6jkhA/result.json"
    df = pandas.read_json(requests.get(url).text)
    output_filename = "{}_{}_{}.csv".format(os.environ['PROJECT_NAME'], os.environ['GIT_BRANCH'], os.environ['GIT_SHA'])
    df.to_csv("s3://{}/{}/{}".format(os.environ['S3_BUCKET'], os.environ['S3_KEY_BASE'], output_filename))

