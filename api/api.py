from newsapi.newsapi_client import NewsApiClient
import requests
import pprint
from datetime import datetime, timedelta, timezone

import flask
from flask import request, jsonify

import json

import nltk
nltk.data.path.append('/whatever')

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

app = flask.Flask(__name__)
app.config["DEBUG"] = True

timerightnow = datetime.now()
timeonedayago = datetime.today() - timedelta(hours=24, minutes=0)

# Summarize API
url = "https://www.nytimes.com/2020/11/06/opinion/sunday/joe-biden-president-policy.html"
LANGUAGE = "english"
SENTENCES_COUNT = 2

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/v1/summary/all', methods=['GET'])
def news_all():
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    summarized = summarizer(parser.document, SENTENCES_COUNT)

    sentence_list = []

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        sentence_list.append(sentence)

    x = {
    	"title" : "article title",
    	"first" : str(sentence_list[0]),
    	"second" : str(sentence_list[1])
    }    

    return jsonify(x)

@app.route('/api/v1/news', methods=['GET'])
def return_articles():
    return get_news_articles() # should be a list of jsons

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
    
def get_news_articles():
    newsapi = NewsApiClient(api_key='1224ab37b05c4c80a1f588ee586b15d7')
    all_articles = newsapi.get_everything(q='election OR biden OR trump OR pandemic OR virus OR stocks OR economy OR politics OR usa OR harris OR pence OR vote',
                                      from_param=timeonedayago,
                                      to=timerightnow,
                                      language='en',
                                      sort_by='relevancy',
                                      page_size=5)
                                      

    json_articles = all_articles['articles']
    summarized_articles = create_cycle_json(json_articles)
 
    return json.dumps(summarized_articles)

def input_article_parse(article_list):
    # list of json objects
    dictionary_article_list = []
    for json_item in article_list:
        dictionary_article_list.append(json_item)
     #= json.loads(article_list)
    parsed_articles = []
    
    for article in dictionary_article_list:
        temp_dict = {}
        temp_dict['url'] = article["url"]
        temp_dict['source'] = article["source"]["name"]
        temp_dict['title'] = article["title"]
        
        parsed_articles.append(temp_dict)

    return parsed_articles

# returns a single json object for a set of articles
def create_cycle_json(articles):
    now = datetime.now()
    cycle_obj = {}
    cycle_obj['date'] = str(now)
    summaries = []
    
    parsed_articles = input_article_parse(articles)
    
    for article in parsed_articles:
        summarized_article = summarize_article(article)
        summaries.append(summarized_article)
        
    cycle_obj['summaries'] = summaries
    
    return cycle_obj
    
# need a method for appending new cycles to json list
    
# returns a dictionary object for 1 article summary
def summarize_article(article):
    # an article summary should be a dictionary object
    url = article['url']
    title = article['title']
    source = article['source']
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    summarized = summarizer(parser.document, SENTENCES_COUNT)
    sentence_list = []
    
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        sentence_list.append(sentence)
        
    summary = { # creates a dictionary object
        "title" : title,
        "url" : url,
        "source" : source,
        "first" : str(sentence_list[0]),
        "second" : str(sentence_list[1])
    }

    return summary


#print(type(get_news_articles()))

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(host='0.0.0.0',debug=True)
