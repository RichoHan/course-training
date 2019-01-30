import json
import time
from collections import Counter

import click
import pandas as pd
import requests


class MapParser:
    geocoding_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'

    def __init__(self, api_key):
        self.api_key = api_key

    def parse_to_coord(self, address):
        request_url = self.geocoding_url.format(
            address=address,
            api_key=self.api_key
        )
        response = requests.get(request_url).json()
        if len(response['results']) > 1:
            print('Not an accurate address.')
            return

        print(json.dumps(
            response['results'][0]['geometry']['location'], indent=2
        ))


@click.command()
@click.option('--key', prompt='Your Geocoding API key')
@click.option('--csv', prompt='Your csv file')
def start_parser(key, csv):
    df = pd.read_csv(csv)

    # A good way to check class distribution
    # print(Counter(df['分公司狀態']))
    # print(Counter(df['公司名稱']))

    # Shorten company name
    df['company'] = df['公司名稱'].map({
        '統一超商股份有限公司': '7-ELEVEN',
        '全家便利商店股份有限公司': 'FamilyMart',
        '萊爾富國際股份有限公司': 'Hi-Life',
        '來來超商股份有限公司': 'OKmart'
    })

    # Transform company status to labels
    # 1: Good
    # 0: Bad
    df['label'] = df['分公司狀態'].map({
        1: 1,
        3: 0,
        4: 0
    })

    # parser = MapParser(key)
    # for address in df.iloc[0:3]['分公司地址']:
    #     print(address)
    #     parser.parse_to_coord(address)
    #     time.sleep(0.01)


if __name__ == "__main__":
    start_parser()
