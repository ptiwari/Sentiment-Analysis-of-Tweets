import sys
import bayesianClassifier
import pickle
import nltk
from TwitterSearch import *
from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance
import drawPieChart

if(len(sys.argv) != 2):
	print 'Should be tsearch  <search term>';
	exit(0);
    
i=0;     
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    print sys.argv[1]
    tso.setKeywords([sys.argv[1]]) # let's define all words we would like to have a look for
    tso.setLanguage('en') # we want to see German tweets only
    tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
    tso.setIncludeEntities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    CONSUMER_KEY = 'SKxOLVcsxlPN68V3g2hAA'
    CONSUMER_SECRET = 'jBc0MUUNebHiIEkkraM7IruUyoSY2OZZyZ7eW6qqYw'
    TOKEN_FILE = 'out/twitter.oauth'
    APP_NAME = ''
    (oauth_token, oauth_token_secret) = oauth_dance(APP_NAME, CONSUMER_KEY,CONSUMER_SECRET)
	#print oauth_token
    ts = TwitterSearch(consumer_key = CONSUMER_KEY,consumer_secret = CONSUMER_SECRET,access_token = oauth_token,access_token_secret = oauth_token_secret)
    tweets = [];
    
    for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
    	#print tweet['text']
    	txt = tweet['text'];
	words =  txt.split();
	#print txt
		#print words[0]
	if(words[0] != "RT"):
    		if(i<=100):
    			
    			tweets.append(tweet['text']);
        		#print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        		i = i+1;
       	 	else:
        		break;
    
    print 'Total Tweets:',len(tweets)    	
    f= open('neutral.pickle');
    nc = pickle.load(f);
    f.close();
    posTweets = [];
    negTweets = [];
    nutrl = [];
    ppolar = bayesianClassifier.NBayesianMethod();
    print "************* Neutral Tweets ********************"
    for t in tweets:
    	#print t
	s = nc.classify(ppolar.features(t));	
	#print t,s	
	if(int(s)!=2):
		ppolar.tweets.append(t);
	else:
		nutrl.append(t);
		print t;
	
    f= open('polar.pickle');
    pc = pickle.load(f);
    f.close();
    print "**************************"
    for t in ppolar.tweets:
	s = pc.classify(ppolar.features(t));
	print t,s
	if(int(s) ==0):
		negTweets.append(t);
	else:
		posTweets.append(t);
       		
    print '# of positive tweets',len(posTweets);
    print '# of negative tweets',len(negTweets);
    print '# of neutral tweets',len(nutrl);
    labels = ['Positive', 'Negative', 'Neutral']
    totalTweets = len(tweets);
    ptweets = len(posTweets);
    ngtweets = len(negTweets);
    nltweets = len(nutrl);
    fracs = [ptweets/float(totalTweets), ngtweets/float(totalTweets), nltweets/float(totalTweets)]
    drawPieChart.drawPie(labels,fracs);	
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
