import pandas as pd
import numpy as np

def KNN(train,test,k):
	score=0
	#for i in train.values:
		#print(i)
	#print(test)
	print("--- KNN: k = {0} ---".format(k))
	classes = []
	for n in range(k):
		for j in range(len(test.columns)):
			distances=[]
			for i in range(len(train.columns)):
				#print(np.sqrt(np.sum(np.square(test.iloc[:,0]-train.iloc[:,i]))))
				distances.append(np.sqrt(np.sum(np.square(test.iloc[:,j]-train.iloc[:,i]))))
			#print(min(distances))
			#print(np.argmin(distances))
			#print("distance",int(float(train.columns[np.argmin(distances)])))
			#print("class", int(float(test.columns[j])))
			minDistanceFromClass=int(float(train.columns[np.argmin(distances)]))
			#print(test.iloc[:,j])
			
			if minDistanceFromClass==int(float(test.columns[j])):
				score=score+1
				classes.append(minDistanceFromClass)
	print()
	print("Classes correctly predicted (KNN): ", score)
	score=score/len(test.columns)
	print("CV KNN Score: ",score, "/{0}".format(k))
	# print(" ------ CLASSES --------\n\n",classes)
	return (score, classes)



	
	