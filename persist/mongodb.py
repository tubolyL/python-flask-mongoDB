import json
from typing import List
from pymongo import MongoClient
import requests

CLUSTER = MongoClient(
    "mongodb+srv://TLevente:BitcoinDB@cluster0.3iezf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB = CLUSTER["Bitcoin"]
COLLECTION = DB["BitcoinPriceData"]
ANALYSIS_COLLECTION = DB["Analysis"]


def search() -> List:
    for document in COLLECTION.find({}):
        data = (document['data'])
    return data


async def upload_calculation_data(calculated_data: float, data_type: str):
    post = {"data_type": data_type, "value": calculated_data}
    return ANALYSIS_COLLECTION.insert_one(post)


def update():
    url = 'http://api.coincap.io/v2/assets/bitcoin/history?interval=d1'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if r.status_code != 429:
        try:
            COLLECTION.delete_many({})
            COLLECTION.insert_one(r.json())
            return 'Update Successful'
        except Exception as e:
            return f'Something went wrong. Error: {e.status_code}'
    else:
        return f'Too many requests. Try again later. (Error: {r.status_code})'


def upload(data):
    try:
        COLLECTION.delete_many({})
        COLLECTION.insert_one(data)
        return 'Update Successful'
    except Exception as e:
        return f'Something went wrong. Error: {e.args}'


if __name__ == '__main__':
    print(search())
