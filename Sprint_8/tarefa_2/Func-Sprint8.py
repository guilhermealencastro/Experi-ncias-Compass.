import json
import os
import boto3
import requests
from datetime import datetime

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_REGION = 'us-east-1'

TMDB_API_KEY = ''
S3_BUCKET_NAME = 'bucketsprint8'
S3_PREFIX = 'Raw/TMDB/JSON/'

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)


def lambda_handler(event, context):
    current_date = datetime.now()
    date_prefix = current_date.strftime('%Y/%m/%d')
    s3_path = f"{S3_PREFIX}{date_prefix}/tmdb_movies_2021_2023.json"

    try:
        tmdb_data = fetch_tmdb_data(start_year=2021, end_year=2023)

        upload_to_s3(json.dumps(tmdb_data), s3_path)

        return {
            'statusCode': 200,
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Erro ao armazenar dados no S3: {str(e)}'
        }


def fetch_tmdb_data(start_year, end_year):
    tmdb_data = []
    page = 1

    while True:
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=27&page={page}&primary_release_date.gte={start_year}-01-01&primary_release_date.lte={end_year}-12-31'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get('results'):
                tmdb_data.extend(data['results'])
                page += 1
            else:
                break
        else:
            raise Exception(f'Erro ao buscar dados do TMDB: {response.text}')

    return tmdb_data


def upload_to_s3(data, s3_path):
    s3.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=s3_path,
        Body=data,
        ContentType='application/json'
)
