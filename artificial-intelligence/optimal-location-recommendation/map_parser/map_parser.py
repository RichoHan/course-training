import json
import os

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
        try:
            response = requests.get(request_url).json()
            if len(response['results']) == 0:
                return None, None, 0

            location = response['results'][0]['geometry']['location']
            return location['lat'], location['lng'], len(response['results'])

        except Exception as e:
            print(e)
            if response:
                print(json.dumps(response, indent=2))
            return None, None, 0

    def download_tile(self, filename, lat, lng):
        img = open(filename, 'wb')
        img.write(
            requests.get(
                'https://api.mapbox.com/styles/v1/richohan/cjrkh81fb1mjp2toa331e5br6/static/{},{},16/300x300?access_token={}'.format(lng, lat, self.api_key)
            ).content
        )
        img.close()


def parse_address(parser, df):
    """ Parse address to latitudes and longitudes. """
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

    # Fill in correspinding coordinates
    with click.progressbar(length=len(df)) as bar:
        for index, row in df.iterrows():
            lat, lng, candidates = parser.parse_to_coord(row['分公司地址'])
            df.loc[index, 'lat'] = lat
            df.loc[index, 'lng'] = lng
            df.loc[index, 'candidates'] = candidates
            bar.update(1)

    df.to_csv('processed-c-stores.csv')


def download_tiles(parser, df):
    """ Download tiles based on latitudes and longitudes. """
    try:
        filtered_df = df.loc[df['candidates'] == 1]
        click.secho(
            'Number of tiles available: {}'.format(len(filtered_df)),
            fg='green'
        )
        with click.progressbar(length=len(filtered_df)) as bar:
            for index, row in df.iterrows():
                bar.update(1)
                invoice, lat, lng = row.loc[['分公司統一編號', 'lat', 'lng']]

                folder = 'maps'
                if not os.path.isdir(folder):
                    os.makedirs(folder)

                filename = '{}.png'.format(invoice)
                if filename in os.listdir(folder):
                    continue

                parser.download_tile(
                    '{}/{}'.format(folder, filename), lat, lng
                )

    except Exception as e:
        print(e)
        click.secho('Wrong format for downloading tiles.', fg='red')


@click.command()
@click.option('--key', prompt='Your API key')
@click.option('--csv', prompt='Your csv file')
@click.option('--mode', prompt='Parse mode')
def start_parser(key, csv, mode):
    parser = MapParser(key)
    df = pd.read_csv(csv)

    if mode == 'geocoding':
        parse_address(parser, df)

    elif mode == 'tiles':
        download_tiles(parser, df)


if __name__ == "__main__":
    start_parser()
