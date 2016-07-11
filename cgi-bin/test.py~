from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt
from sys import argv
import cPickle



with open('../file/Model.pkl', 'rb') as fid:		
	rf = cPickle.load(fid)
	test=[]
	

	target = open("../file/test.txt", 'r')
	lines=target.read().split("\r\n")
	

	for index in lines:
		if len(index)!=0:
			line=index.split(",")
			test.append([int(line[0]) , long(line[1]), int(line[2]) , int(line[3]) , int(line[4]) , int(line[5]) , int(line[6]) , float(line[7]) , float(line[8])])
				
	
	target.close()
	result=rf.predict(test)
	target = open("../file/test.txt", 'w')

	for index in result:
		target.write(str(index))
		target.write("\r\n")
	
	target.close()
		
		
			
	   	

