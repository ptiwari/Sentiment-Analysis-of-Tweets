import csv
import math
import nltk
import pickle
import re
#import myNaivBayes

class NBayesianMethod:

	def features(self,document):
		featureSet = {}
		
		#document = re.sub("[\.\t\,\:;\(\)\.]", "", document, 0, 0)
		
		words = document.split();
		#if(len(words)>1):
		#	words = words[1:len(words)];
		self.stopwords=[];
		for w in words:
			#nw = w.lower();
			nw = w;	
			if not nw in self.stopwords:
				self.feat.append(w);
				featureSet['contains(%s)' % nw] = 'True'	
		
		return featureSet
	

	
	def __init__(self,trainFile=None,type=1):
		self.tweets=[];
		self.readStopWords('stopwords.txt');
		self.feat = [];
		if(trainFile != None):
			
			if(type=='1'):
				print "Reading Neutral File"
				self.readFileNeutral(trainFile);
			else:
				print "Reading polar file"
				self.readFilePolarity(trainFile);
			self.numFeatures = 0;
		#self.readFile(testFile,self.testingTweets)
		#print self.traingTweets;
		#print 'Testing Tweets'
		#print self.testingTweets;
		
	def readStopWords(self,sfile):
		f = open(sfile,'r');
		self.stopwords=[];
		for line in f:
			self.stopwords.append(line.strip('\n')); 
			
	def readFilePolarity(self,inputfile):
		fp = open( inputfile,'rU')
		reader = csv.reader(fp);
		self.pos = 0;
		self.neg = 0;
		self.neut = 0;
		for r in reader:
			if(int(r[0])==4):
				self.pos = self.pos + 1;
			elif(int(r[0])==0):
				self.neg = self.neg + 1;
			else:
				self.neut = self.neut + 1;
			if(int(r[0])!=2):
				self.tweets.append((r[5],r[0]));
			
		#print "Positive",pos,"Negative:",neg,"Neutral",neut
						
	def readFileNeutral(self,inputfile):
		fp = open( inputfile,'rU')
		reader = csv.reader(fp);
		self.pos = 0;
		self.neg = 0;
		self.neut = 0;
		for r in reader:
			if(int(r[0])==4):
				self.pos = self.pos + 1;
			elif(int(r[0])==0):
				self.neg = self.neg + 1;
			else:
				self.neut = self.neut + 1;
			if(int(r[0])!=2):
				r[0] = '4';	
				self.tweets.append((r[5],r[0]));
			else:
				self.tweets.append((r[5],r[0]));
		#print "Positive",pos,"Negative:",neg,"Neutral",neut

	
	def trainClassifier(self,clfileName):		
		
		train_set = [(self.features(d),s) for (d,s) in self.tweets]
		unq = set(self.feat)
		print "Number of features",len(unq);
		#train_set = [(self.createFeatures(self.posTweets),4)];
		#train_set.append((self.createFeatures(self.negTweets),0));	
		#print train_set
		#cl = myNaivBayes.train(train_set);
		classifier = nltk.NaiveBayesClassifier.train(train_set);
		print "Number of Features",self.numFeatures;
		f = open(clfileName, 'wb')
		pickle.dump(classifier, f)
		f.close()
		#tweets = [self.features(d) for (d,s) in self.testingTweets]
		#for (t,s) in self.testingTweets:
		#	print t, classifier.classify(self.features(t));
		#print 'Accuracy:',nltk.classify.accuracy(classifier, [(self.features(d),s) for (d,s) in self.testingTweets])
'''	def testClassifier(self):
		
		testTweets = [d for (d,s) in self.testingTweets];
		print 'Testing Tweets';
		print testTweets
		#print nltk.classify(self.classifier, [self.features(d) for (d,s) in self.testingTweets])
'''	