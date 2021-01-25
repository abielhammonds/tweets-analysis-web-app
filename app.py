from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    
   # if request has args (?tweet=some_tweet)
    if request.args:

        # get the value of the arg
        tweet = request.args.get('tweet')   
        
        return tweet

    return 'Hello World!'

@app.route('/about')
def about():

    about_text = """
    This is a Sentiment Analysis app for tweets!
    \n Designed by: A'Biel Hammonds, Aleia Parker, Ngoc Nguyen, and Brandi Huesmann
    """
    return about_text


if __name__=='__main__':

     app.run(debug=True)


