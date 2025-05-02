from google.cloud import storage
import os

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Example Usage
upload_blob('retail-data', 'data/sample_transactions.csv', 'transactions/2025-04-30/sample_transactions.csv')
upload_blob('retail-data', 'data/sample_macro.csv', 'macro/sample_macro.csv')
