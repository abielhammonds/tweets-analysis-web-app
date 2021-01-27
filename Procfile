# This file tells Heroku that we are deploying a 'web' app. 
# It then runs the command 'python start.py' to download the nltk files.
# Finally gunicorn runs our app called app.py. 

web: python start.py && gunicorn app:app