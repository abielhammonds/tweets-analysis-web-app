from flask import Flask
from flask import request
from flask import render_template

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag

from joblib import load
import re, string
re
app = Flask(__name__)

@app.route('/')
def home():
    '''This is the home route. It only handles GET requests. It will return the templates/index.html file.'''
 
    return render_template('index.html') # return the html file under templates foldertemplate('index.html')
  
  

# Home route that does allow POST requests.
@app.route('/',methods=['POST'])
def analyze():
    '''This route will handle for submission. When a POST request is received this code will run.'''

    
    # clean the tweet and return tokens. This is from previous work.
    def remove_noise(tweet_tokens, stop_words = ()):

        cleaned_tokens = []

        for token, tag in pos_tag(tweet_tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                        '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
            token = re.sub("(@[A-Za-z0-9_]+)","", token)

            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
                cleaned_tokens.append(token.lower())
        return cleaned_tokens

    # load the saved classifier
    clf = load('tweet_classifier.joblib')

    custom_tweet = request.form.get('text') # get the text from the html form that was submitted. 
    
    # prep tweet for sentiment analysis
    custom_tokens = remove_noise(word_tokenize(custom_tweet))

    # get the sentiment
    sentiment = clf.classify(dict([token, True] for token in custom_tokens))
    
    # return our html template with the variables to be injected
    return render_template('index.html',tweet = custom_tweet, sentiment = sentiment)



@app.route('/about')
def about():

    about_text = """
    This is a Sentiment Analysis app for tweets!
    \n Designed by: A'Biel Hammonds, Aleia Parker, Ngoc Nguyen, and Brandi Huesmann
    """
    return about_text


if __name__=='__main__':

     app.run(debug=True)