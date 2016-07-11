from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt
import cPickle


def Train():
		
	#create the training & test sets, skipping the header row with [1:]

        dataset = genfromtxt(open('../file/Train.csv','r'), delimiter=',', dtype='str')[1:] 
   	train=[]
	target=[]

	for x in dataset:

        	train.append([int(x[0]),long(x[1]),int(x[2]),int(x[3]),int(x[4]),int(x[5]),int(x[6]),float(x[7]),float(x[8])])
		target.append([x[9]])

        #create and train the random forest
        #multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)

        rf = RandomForestClassifier(n_estimators=100)
        rf.fit(train, target)
	
	# save the classifier
	with open('../file/Model.pkl', 'wb') as fid:
    		cPickle.dump(rf, fid)

Train()


