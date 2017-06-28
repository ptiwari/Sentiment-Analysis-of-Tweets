#!/usr/bin/env python
# encoding: utf-8
 
import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
from twitter.oauth_dance import oauth_dance

#Twitter API credentials

consumer_key = 'SKxOLVcsxlPN68V3g2hAA'
consumer_secret = 'jBc0MUUNebHiIEkkraM7IruUyoSY2OZZyZ7eW6qqYw'
access_key = ""
access_secret = ""
 
 
def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	(access_key, access_secret) = oauth_dance('', consumer_key,consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	tweets=[];
	fname = '%s_tweets.txt' % screen_name;
	print fname
	f = open(fname,'w');
	for t in outtweets:
		txt = t[2];
		words =  txt.split();
		#print words[0]
		if(words[0] != "RT"):
			f.write(txt);
			f.write('\n');
		
 	f.close();
if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets(sys.argv[1])