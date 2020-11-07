from newsapi.newsapi_client import NewsApiClient
import json

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


for thing in all_articles['articles']:
  print(json.dumps(thing, indent=4))