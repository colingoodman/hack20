from newsapi.newsapi_client import NewsApiClient
import json
import requests
import pprint
from datetime import datetime, timedelta, timezone

timerightnow = datetime.now()
print(timerightnow.strftime('%Y-%m-%dT%H:%M:%S'))

fourhoursago = datetime.today() - timedelta(hours=24, minutes=0)
print(fourhoursago.strftime('%Y-%m-%dT%H:%M:%S'))

# Init
newsapi = NewsApiClient(api_key='59cc7898a9774af8bce9ea1b0ebb6e50')

all_articles = newsapi.get_everything(q='election OR biden OR trump OR pandemic OR virus OR stocks OR economy OR politics OR usa OR harris OR pence OR vote',
                                      from_param=fourhoursago,
                                      to=timerightnow,
                                      language='en',
                                      sort_by='relevancy',
                                      page_size=5)


for thing in all_articles['articles']:
  print(json.dumps(thing, indent=4))

print(type(all_articles['articles']))
print(len(all_articles['articles']))

