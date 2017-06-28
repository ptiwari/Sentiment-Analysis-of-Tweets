import sys
import bayesianClassifier

def main():
	if len(sys.argv)!=4:
		print 'Invalid Command. Should be python MainHandler train_file classifier_file type(1:Neutral,2:Polarity) ';
		sys.exit(0);
	
	print sys.argv[1];
	pdata = bayesianClassifier.NBayesianMethod(sys.argv[1],sys.argv[3]);
	pdata.trainClassifier(sys.argv[2]);
	#pdata.testClassifier();
			
if __name__ == '__main__':
  main()