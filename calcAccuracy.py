import sys
import bayesianClassifier
import pickle
import nltk

def main():

	if len(sys.argv)!=2:
		print 'Invalid Command. Should be python MainHandler test_file ';
		sys.exit(0);
	
	f= open('neutral.pickle');
	classifier = pickle.load(f);
	f.close()
	pdata = bayesianClassifier.NBayesianMethod(sys.argv[1],"1");
	alltweets=[];
	print 'Accuracy:',nltk.classify.accuracy(classifier, [(pdata.features(d),s) for (d,s) in pdata.tweets])
	for (t,s) in pdata.tweets:
		p = classifier.classify(pdata.features(t));
		alltweets.append((t,p,s));
	f= open('polar.pickle');
	classifier = pickle.load(f);
	f.close()
	pdata = bayesianClassifier.NBayesianMethod(sys.argv[1],2);
	print 'Accuracy:',nltk.classify.accuracy(classifier, [(pdata.features(d),s) for (d,s) in pdata.tweets])

	print 'Tweet \t\t\t Actual \t\t Predicted';
	wrong = 0;
	for (t,s) in pdata.tweets:
		p = classifier.classify(pdata.features(t));
		alltweets.append((t,p,s));
	for (t,p,s) in alltweets:
		if p !=s:
			print p,s
			print t,'\t',s,'\t',p;	
			wrong = wrong + 1;
	print wrong
	print "Accuracy:",float(wrong)/len(pdata.tweets);
		
	
if __name__ == '__main__':
  main()