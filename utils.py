# encoding=utf8

import nltk
from nltk import word_tokenize
from nltk import PorterStemmer
from nltk.corpus import stopwords
# import pymysql
from nltk.stem.porter import *
import string

stop_words = set(stopwords.words("english"))
secstopwords = ['bull', 'kernelmodeinfo', 'view', 'topic', 'attach', 'thank', 'lot', 'I', 'ok',
                'code', 'string', 'year', 'final', 'true', 'var', 'fals','as', 'told','if', 'what', 'appear', 'String',
                'attach', 'jpg', 'my', 'If', 'hxxp', 'We', 'It', 'who', 'tell', 'also', 'take', 'use', 'thread', 'OK'
                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                ]

stemmer = PorterStemmer()
punctuations = '''!()-[]{};:'"|\,=+<>./?@#$%^&`*_~'''
stop_string_list = ['kernelmode', 'https', 'http', 'virustotal', 'view', 'wwwgoogleanalyticscom', 'connectfacebooknet', 'this','hxxp', 'yahoocom', 'bingcom', '0daytoday']

def preprocessor(str):
    """
    input a string to be cleaned
    remove punctuation, tokenize phrase, filter our stop-words, stem accordingly
    :return:pre-processed text
    """
    # pre-processing utilities: stemming, stopword and punctuations lists

    no_punct = ""
    for char in str:
       if char not in punctuations:
           no_punct = no_punct + char

    tokenized_text = word_tokenize(no_punct)
    filteredPhrasedefault = [word for word in tokenized_text if word not in stop_words]
    filteredPhrase = [word for word in filteredPhrasedefault if word not in secstopwords]

    # stemmedfilteredphrase = [stemmer.stem(word) for word in filteredPhrase]
    # filteredPhrasedefault = [word for word in stemmedfilteredphrase if word not in stop_words]
    # filteredPhrase = [word for word in filteredPhrasedefault if word not in secstopwords]

    l = filteredPhrase

    for s in stop_string_list:
        l = [w for w in l if s not in w]

    l = [x for x in l if 3 < len(x) <= 20]
    l = [x for x in l if not x.isdigit()]

    return l

# # TODO: Change DB connection credential
# def db_connect():
#     return pymysql.connect(host="localhost", user="root", passwd="root", db="cybersecurity6_2017",charset='utf8', autocommit=True)