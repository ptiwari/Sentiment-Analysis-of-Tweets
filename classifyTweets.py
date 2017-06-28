import sys
import bayesianClassifier
import pickle
import nltk

def main():

	if len(sys.argv)!=4:
		print 'Invalid Command. Should be python MainHandler test_file classifier_file type(1:neutral,2:polar)';
		sys.exit(0);
	
	f= open(sys.argv[2]);
	classifier = pickle.load(f);
	f.close()
	pdata = bayesianClassifier.NBayesianMethod(sys.argv[1],sys.argv[3]);
	
	print 'Accuracy:',nltk.classify.accuracy(classifier, [(pdata.features(d),s) for (d,s) in pdata.tweets])

	print 'Tweet \t\t\t Actual \t\t Predicted';

#	for (t,s) in pdata.tweets:
#		p = classifier.classify(pdata.features(t));
#		if p !=s:
#			print t,'\t',s,'\t',p;	
		
	
if __name__ == '__main__':
  main()