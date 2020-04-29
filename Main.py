import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet') 
nltk.download('treebank')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

data=input("Enter the text \n")

import numpy as np
import pandas as pd
import re
import heapq

formatted_text = re.sub('[^a-zA-Z]', ' ', data )
formatted_text = re.sub(r'\s+', ' ', formatted_text)

sent_list = nltk.sent_tokenize(data)
stopwords = nltk.corpus.stopwords.words('english')

word_freq = {}
for w in nltk.word_tokenize(formatted_text):
    if w not in stopwords:
        if w not in word_freq.keys():
            word_freq[w] = 1
        else:
            word_freq[w] += 
            
  max_freq = max(word_freq.values())

for w in word_freq.keys():
    word_freq[w] = (word_freq[w]/max_freq)
    
sent_scores = {}
for s in sent_list:
    for word in nltk.word_tokenize(s.lower()):
        if w in word_freq.keys():
            if len(s.split(' ')) < 20:
                if s not in sent_scores.keys():
                    sent_scores[s] = word_freq[w]
                else:
                    sent_scores[s] += word_freq[w]
                    
 
summary_sent = heapq.nlargest(4, sent_scores, key=sent_scores.get)

summary = ' '.join(summary_sent)
print(summary)
    
