import csv
import math
class ProcessData:

	def getIDF(self,numdocs,term_num_docs):	
		return math.log(float(1 + numdocs) / (1 + term_num_docs))
		
	def getTF(self,d,t):
		c= d.count(t);
		tf = float(c)/len(d);
	
		return tf;
	
	def get_word_features(self,wordlist):
		wordlist = nltk.FreqDist(wordlist)
		word_features = wordlist.keys()
		print wordlist
		return word_features
		
	def __init__(self,inputfile):
		fp = open( inputfile,'rU')
		reader = csv.reader(fp);
		self.tweets_senti =[];
		
		i=0;
		self.allwords=[];
		for r in reader:
			print r
			if(int(r[0])==0 and i<=5000):
				i=i+1;
				self.tweets_senti.append((r[5],-1));
				for w in r[5].split():
					self.allwords.append(w);
			elif(int(r[0])==4 and i <=10000):
				i=i+1;
				self.tweets_senti.append((r[5],1));
				for w in r[5].split():
					self.allwords.append(w);
		#print 'AllWords',documents
		self.unqwords = list(set(self.allwords));
		#print 'all words',len(unqwords);
		print 'unique wors',len(self.allwords);
		print '# of Tweets',len(self.tweets_senti);
		
		
	def createMatrixOfTweets(self,matrixfile,labelfile,dictfile):
		i=1;
		numdocs = len(self.tweets_senti);
		print 'numdocuments',numdocs
		ft = open(matrixfile,'w');  
		flabel = open(labelfile,'w');
		for (d,sentiment) in self.tweets_senti:
			#print d
			for w in d.split():
				row = self.unqwords.index(w);
				row = row + 1;
				term_num_docs = self.allwords.count(w);
				print w,term_num_docs
				tf = self.getTF(d,w);
				idf = self.getIDF(numdocs,term_num_docs);
				freq = tf*idf;
				#print w,'tf:',tf,'Idf:',idf,freq
				ft.write(str(row)+' '+str(i)+' '+str(freq));
				ft.write('\n');
			flabel.write(str(sentiment));
			flabel.write('\n');
			i = i+1;
		
		ft.close();
		flabel.close();
		f = open(dictfile,'w');  
		for w in self.unqwords:
			f.write(w);
			f.write('\n');
		f.close();
