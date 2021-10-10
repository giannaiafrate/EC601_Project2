import requests
import os
import json
import csv

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

# Various keywords depend on the different teams, each team will use their 
# team name and 2021 team hashtag. Teams and hashtags are below:

# AL Central:                   AL East:                    AL West:
# White Sox #ChangeTheGame      Orioles #Birdland           Astros #ForTheH
# Indians #OurCLE               Red Sox #DirtyWater         Angels #WeBelieve
# Tigers #DetroitRoots          Yankees #SquadUp            Athletics #RiseAndGrind
# Royals #TogetherRoyal         Blue Jays #WeAreBlueJays    Mariners #SeaUsRise
# Twins #MNTwins                Rays #RaysUp                Rangers #StraightUpTX

# NL Central:                   NL East:                    NL West:
# Cubs #CubTogether             Braves #ForTheA             Diamondbacks #RattleOn
# Reds #ATOBTTR                 Marlins #JuntosMiami        Rockies #Rockies
# Brewers #ThisIsMyCrew         Mets #LGM                   Dodgers #Dodgers
# Pirates #LetsGoBucs           Phillies #RingTheBell       Padres #HungryForMore
# Cardinals #STLFLY             Nationals #NATITUDE         Giants #ResilientSF

search_url = "https://api.twitter.com/2/tweets/search/recent"
keyword="red sox"
max_results=100
csvOutput = open('RedSox_Tweets.csv','a')
csvWriter=csv.writer(csvOutput)
query_params = {'query': keyword,'max_results': max_results,'tweet.fields': 'author_id'}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    [attribute,value]=json_response.items()
    outresponse=(attribute[1])

    for tweets in outresponse:
        currenttweet=tweets['text']
        first1str=currenttweet[0]
        first2str=first1str+currenttweet[1]
        isretweet=first2str=="RT"
        isreply=first1str=="@"
        if isretweet==0:
            if isreply==0:
                print([currenttweet])
                csvWriter.writerow([currenttweet])

if __name__ == "__main__":
    main()
