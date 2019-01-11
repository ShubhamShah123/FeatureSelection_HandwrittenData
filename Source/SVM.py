import pandas as pd
import numpy as np
from sklearn.svm import SVC
import warnings
warnings.filterwarnings("ignore")
#train = pd.read_csv("train.csv")
#test = pd.read_csv("test.csv")

def SVM(train,test):
	print("--- Supprt Vector Machines ---")
	noOfObjectsInAClass=0
	for i in range(len(train.columns)):
		if i > 0:
			if int(float(train.columns[i-1])) - int(float(train.columns[i])) < 0:
				break
			else:
				noOfObjectsInAClass=noOfObjectsInAClass+1
		else:
			noOfObjectsInAClass=noOfObjectsInAClass+1
	noOfClasses=int(len(train.columns)/noOfObjectsInAClass)

	trainLabels=[]
	for j in range(0,len(train.columns),noOfObjectsInAClass):
			for k in range(0,noOfObjectsInAClass):
				trainLabels.append(train.columns[j])

	#print(trainLabels)
	#print(train.transpose())


	clf = SVC(gamma='auto')
	clf.fit(train.transpose(), trainLabels)

	#print(test.transpose())
	answers=clf.predict(test.transpose())
	score=0
	classes = []
	for i in range(len(answers)):
		#print(int(float(answers[i])),",",int(float(test.columns[i])))
		if int(float(answers[i]))==int(float(test.columns[i])):
			score=score+1
			classes.append(answers[i])
	print()
	print("Classes correctly predicted (SVM): ", score)
	score=score/len(test.columns)
	print("CV SVM Score: ",score, "/1.0")
	# print("SVM Classes: \n",classes)
	return (score, classes)