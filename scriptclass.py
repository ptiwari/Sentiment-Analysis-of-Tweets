import sys
import bayesianClassifier
import pickle
import nltk
f= open('neutral.pickle');
nc = pickle.load(f);
f.close()
ffeatred = open('neutral_woswrds.pickle');
ncred = pickle.load(ffeatred);
ffeatred.close()
f= open('polar.pickle');
pc = pickle.load(f);
f.close()
pdata = bayesianClassifier.NBayesianMethod('ltest.csv');

