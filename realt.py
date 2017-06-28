import sys
import bayesianClassifier
import pickle
import nltk
from TwitterSearch import *
from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

def features(document):
	#print document
	featureSet = {}
	for word in document.split():
		#print word
		featureSet['contains(%s)' % word] = (word in document)
	return featureSet
		

    
ft = open('realtweets.txt');

tweets = [];
for line in ft:
	tweets.append(line);
 


f= open('my_classifier.pickle');
classifier = pickle.load(f);
posTweets = [];
negTweets = [];
for t in tweets:   
	s = classifier.classify(features(t));		
	if(int(s)==4):
		posTweets.append(t);
	else:
		negTweets.append(t);
print 'Positive Tweets';
print posTweets;
print 'Negative Tweets'
print negTweets;	
print '# of positive tweets',len(posTweets);
print '# of negative tweets',len(negTweets);
	
