from newsapi.newsapi_client import NewsApiClient
import json
import requests

# Init
newsapi = NewsApiClient(api_key='1224ab37b05c4c80a1f588ee586b15d7')

all_articles = newsapi.get_everything(q='election',
                                      sources='fox-news',
                                      domains='foxnews.com',
                                      from_param='2020-11-06T00:00:00',
                                      to='2020-11-07T00:00:00',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

top_articles = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=1224ab37b05c4c80a1f588ee586b15d7')


for thing in all_articles['articles']:
  print(json.dumps(thing, indent=4))

top_articles = top_articles.json()

# print to a JSON file
# will contain top headlines
# ordered from least recent to most recent
with open('data.txt', 'w') as outfile:
  print(json.dumps(top_articles['articles'], indent=4))

print(type(top_articles['articles']))
print(len(top_articles['articles']))

