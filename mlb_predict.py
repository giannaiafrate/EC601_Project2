import sys
from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1
from google.oauth2.credentials import Credentials
from google.cloud import language_v1

if __name__ == '__main__':
    file_path = sys.argv[1]
    model_name = sys.argv[2]
    options = ClientOptions(api_endpoint='automl.googleapis.com')
    prediction_client = automl_v1.PredictionServiceClient(client_options=options)
    #payload = inline_text_payload(file_path)
    with open(file_path, 'rb') as ff:
        content = ff.readlines()
        for line in content:
            #print(line)
            payload = {'text_snippet': {'content': line, 'mime_type': 'text/plain'} }
            params = {}
            request = prediction_client.predict(name=model_name, payload=payload)
            #csvWriter.writerow([request])
            newrequest=str(request)
            lister=newrequest.split('\n')
            newlist=list()
            for item in lister:
                newlist.append(item.strip(' '))
            sentimentscore=newlist[2]
            sentimentvalue=newlist[7]
            if sentimentscore[0] == 's':
                print(sentimentscore,sentimentvalue)
