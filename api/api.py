import flask
from flask import request, jsonify

# from newsapi import NewsApiClient

# Init
# newsapi = NewsApiClient(api_key='1224ab37b05c4c80a1f588ee586b15d7')

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# @app.route("/")
# def homepage():
#     return render_template("page.html", title="HOME PAGE")

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

# articles = []

# all_articles = newsapi.get_everything(q='election',
#                                       sources='fox-news',
#                                       domains='foxnews.com',
#                                       from_param='2020-11-06T00:00:00',
#                                       to='2020-11-07T00:00:00',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=1)

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

# @app.route('/api/v1/news/all', methods=['GET'])
# def news_all():
#     return jsonify(all_articles)

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    #app.run(debug=True)