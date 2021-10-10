import requests, os, json
import pandas as pd
import csv
import datetime, dateutil.parser
import unicodedata, time

# set up environment with token
# retrieve token from environment
def auth():
    return os.getenv('TOKEN')

# function that will take bearer token
def create_headers(bearer_token):
    headers={"Authorization": "Bearer {}".format(bearer_token)}
    return headers

# create url to pull
def create_url(keyword, start_date, end_date, max_results = 10):
    # search_url is one of the endpoints
    search_url="https://api.twitter.com/2/tweets/search/all"
    # customizing the request we send
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}} # get next page of results
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token=None):
    params['next_token']=next_token
    response = requests.request("GET",url, headers=headers, params=params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code,response.text)
    return response.json()
    # response code 200 is when the get request goes through and everything is correct

bearer_token=auth()
headers=create_headers(bearer_token)
keyword = "xbox lang:en"
start_time = "2021-03-01T00:00:00.000Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 15

url = create_url(keyword,start_time, end_time, max_results)
json_response = connect_to_endpoint(url[0],headers,url[1])

print(json.dumps(json_response, indent=4, sort_keys=True))


"""
url = 'https://api.twitter.com/2/tweets/search/recent?query=%2523caturday%2520has%253Aimages%2520-is%253Aretweet'
headers='Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAHZhUAEAAAAA7fnRnCW%2BzJ5Ko%2BueOSPnIA96xqU%3DIxr8hKBP8f63LmzSSGEycrstTLn4kIQsROwMauK2iL4oMrI7ze'

r = requests.post(url, headers=headers)
"""
