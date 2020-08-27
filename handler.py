import json
import requests
import pandas


def run(event, context):
    url = "https://cache1.phantombooster.com/ukZxdjCQmz0/Vg7zuvUGSEG6yzglJ6jkhA/result.json"
    request = requests.get(url)
    list_of_dicts_data = request.json()
    print(len(list_of_dicts_data))
