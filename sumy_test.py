from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import json

LANGUAGE = "english"
SENTENCES_COUNT = 2


if __name__ == "__main__":
    url = "https://www.nytimes.com/2020/11/06/opinion/sunday/joe-biden-president-policy.html"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    
    summarized = summarizer(parser.document, SENTENCES_COUNT)
    
    #print(summarized)
    sentence_list = []

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        sentence_list.append(sentence)
        
    x = {
    	"title" : "article title",
    	"first" : str(sentence_list[0]),
    	"second" : str(sentence_list[1])
    }    
    
    json_obj = json.dumps(x)
        
    print(json.loads(json_obj))
    with open('file.json','w') as outfile:
    	json.dump(x, outfile)

		
		
		
		
		
		
		
		

