# Text Summarization

Made use of nltk, re and heapq modules. The paragraph is taken as input from the user in the form
of a string. The data is made free of punctuation and replace with spaces using the sub function from
re module (re.sub()). This formatted data is now tokenized into sentences using sent_tokenize from
nltk module. Post eliminating the stop words, the data is tokenized into words and the weighted
frequency of each word in the formatted data is determined and stored as dictionary word_freq.
Similarly sentence scores are calculated and stored in a dictionary sent_scores. The limit for the
number of words in a sentence is kept 20 as we do not want large sentences in the summary. If a
sentence doesn’t exist, it is added to the dictionary as the key with the frequency added to the
current value. From this dictionary, the top n sentences are taken using nlargest function from the
heapq module. I considered 4 here because a short summary is expected. Finally, the summary is
displayed.
