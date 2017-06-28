import sys
import processdata

def main():
	print len(sys.argv)
	if len(sys.argv)!=5:
		print 'Invalid Command. Should be python MainHandler input_file matrix_file label_file dictionary_file';
		sys.exit(0);
	
	print sys.argv[1];
	pdata = processdata.ProcessData(sys.argv[1]);
	pdata.createMatrixOfTweets(sys.argv[2],sys.argv[3],sys.argv[4])
			
if __name__ == '__main__':
  main()