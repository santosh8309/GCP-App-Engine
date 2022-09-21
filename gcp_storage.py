import requests
import json
from google.cloud import storage
# import os


PROJECT_ID = 'rosy-element-362912'
STORAGE_CLIENT = storage.Client(project=PROJECT_ID)

# public rest api endpoint
url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'

# json data
usa_pop_data = requests.get(url).json()

# creating the bucket
bucket_name = "us-population-test-data"
bucket = STORAGE_CLIENT.bucket(bucket_name)
bucket.create()

# uploading the data to GCS bucket
blob = bucket.blob("USA-Population-Data.json")
blob.upload_from_string(data=json.dumps(usa_pop_data),
                        content_type='application/json')


# for bucket in STORAGE_CLIENT.list_buckets():
#     print(bucket)

# command line
# gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_ID --default-storage-class=STORAGE_CLASS --location=BUCKET_LOCATION --uniform-bucket-level-access
