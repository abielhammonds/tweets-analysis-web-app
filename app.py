from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    
  return render_template('index.html')

@app.route('/about')
def about():

    about_text = """
    This is a Sentiment Analysis app for tweets!
    \n Designed by: A'Biel Hammonds, Aleia Parker, Ngoc Nguyen, and Brandi Huesmann
    """
    return about_text


if __name__=='__main__':

     app.run(debug=True)