#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1

def inline_text_payload(file_path):
    with open(file_path, 'rb') as ff:
        content = ff.read()
    return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def pdf_payload(file_path):
    return {'document': {'input_config': {'gcs_source': {'input_uris': [file_path] } } } }

def get_prediction(file_path, model_name):
    options = ClientOptions(api_endpoint='automl.googleapis.com')
    prediction_client = automl_v1.PredictionServiceClient(client_options=options)

    payload = inline_text_payload(file_path)
    # Uncomment the following line (and comment the above line) if want to predict on PDFs.
    # payload = pdf_payload(file_path)

    params = {}

    request = prediction_client.predict(name=model_name, payload=payload)

    return request  # waits until request is returned

if __name__ == '__main__':
    file_path = sys.argv[1]
    model_name = sys.argv[2]

    print(get_prediction(file_path, model_name))

# to run:
 #   python google_predict.py 'YOUR_SOURCE_FILE' projects/641948024261/locations/us-central1/models/TST4290089862419185664