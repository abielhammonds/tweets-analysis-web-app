# A script to download the necessary nltk files for pre-processing.

import nltk
print('Running startup.py...............................')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')