#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import string
from itertools import chain
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier as nbc
from nltk.corpus import CategorizedPlaintextCorpusReader
from textblob import TextBlob
import nltk
from nltk.probability import FreqDist, DictionaryProbDist, ELEProbDist, sum_logs
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify.scikitlearn import SklearnClassifier




s = socket.socket()         # Create a socket object
host = '127.0.0.1'           # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(10)
while 1:
    sc, address = s.accept()   # Now wait for client connection.
    lines = [line.rstrip('\n') for line in open('C:/Users/Raj/Desktop/movies/temp.txt')]
    print (lines)
    Example_Text='\n'.join(lines)
    print ((Example_Text))
    mydir ='C:/Users/Raj/Desktop/movies/cookbook'
    mr = CategorizedPlaintextCorpusReader(mydir, r'(?!\.).*\.txt', cat_pattern=r'(neg|pos)/.*')
    stop = stopwords.words('english')
    documents = [([w for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]

    word_features = FreqDist(chain(*[i for i,j in documents]))
    word_features = list(word_features.keys())[:1000]
    #print(word_features)

    numtrain = int(len(documents) * 90 / 100)
    print(numtrain)
 
    train_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[:numtrain]]
    test_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag  in documents[numtrain:]]



    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, test_set))*100)
    revline= Example_Text.splitlines()
    for x in revline:
        print (x)
        doc = word_tokenize(x.lower())
        featurized_doc = {i:(i in doc) for i in word_features}  #Check this how dictionary is being made
        tagged_label = classifier.classify(featurized_doc)
        print(tagged_label)
        f = open('C:/Users/Raj/Desktop/movies/sentiment.txt','a')
        f.write(tagged_label+'\n') # python will convert \n to os.linesep
        f.close()
    sc.close()
s.close()
