import nltk;
import csv

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    print wordlist
    return word_features
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
fp = open( 'sentiment_train.csv','rb')
reader = csv.reader(fp);
pos_tweets=[];
neg_tweets = [];
i=0;
for r in reader:
	#print r[5]
	if(int(r[0])==0 and i<=500):
		i=i+1;
		#print 'negative';
		neg_tweets.append((r[5],'negative'));
	elif(int(r[0])==4 and i <=1000):
		i=i+1;
		pos_tweets.append((r[5],'positive'));

print '#of positive:',len(pos_tweets), ' #of Negative',len(neg_tweets);
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))
#print tweets;
word_features = get_word_features(get_words_in_tweets(tweets))
training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
#print classifier.show_most_informative_features(32)
#tweet = ' Prachanda could easily lose both Siraha and KTM seats.';
tweet = 'If UML people and  NC people  each other, Prachanda could easily lose both Siraha and KTM seats'
print classifier.classify(extract_features(tweet.split()))
