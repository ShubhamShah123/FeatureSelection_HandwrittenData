import pandas as pd
import numpy as np

#train = pd.read_csv("train.csv")
#test = pd.read_csv("test.csv")

def Centroid(train,test):
	#getting the classItems

	print("--- Centroid ---")

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




	avgs=[]
	trainLabels=[]
	for k in range(0,len(train.columns),noOfObjectsInAClass):
		trainLabels.append(int(float(train.columns[k])))
		#avgs.append(train.columns[k])
	#print(trainLabels)

	index=0
	for j in range(0,len(train.columns),noOfObjectsInAClass):
		#print(train.iloc[:,j:j+noOfObjectsInAClass])
		avg=[[]]
		avg=train.iloc[:,j:j+noOfObjectsInAClass]
		
		#print(np.sum(avg,axis=1)/noOfObjectsInAClass)
		#tempArray=[[]]
		tempArray=np.sum(avg,axis=1)/noOfObjectsInAClass
		#tempArray=avg.sum(axis=1)
		#tempArray2=np.transpose(tempArray)
		#tempArray3=tempArray.transpose()
		#df1 = pd.DataFrame(data=tempArray)
		#tempArray4=df1.train
		#print(tempArray)
		#np.savetxt("check.csv",tempArray, fmt='%i',delimiter=',', newline='\n')
		#print(tempArray)
		#print(np.sum(train.iloc[:,j:j+noOfObjectsInAClass],axis=1))
		#print("temp", type(tempArray))
		#print("avg", type(avgs))
		if index==0:
			avgs=tempArray
			index=index+1
			#print(avgs)
		else:
			#print("hi")
			#avgs=np.concatenate((avgs,tempArray),axis=1)
			#avgs=np.append(avgs,tempArray, axis=1)
			#np.insert(avgs,index,tempArray,axis=1)
			#np.column_stack((avgs,tempArray))
			#avgs=np.hstack((avgs,tempArray))
			avgs=np.vstack((avgs,tempArray))
			index=index+1
	avgs=avgs.transpose()
	avgs=np.vstack((trainLabels,avgs))

	np.savetxt("avgs.csv",avgs, fmt='%f',delimiter=',', newline='\n')
	#print(avgs)


	"""
		if i > 0:
				if (float(train.values[i-1])-float(train.values[i]))>1:
					break
				else:
					noOfObjectsInAClass=noOfObjectsInAClass+1
		else:
			noOfObjectsInAClass=noOfObjectsInAClass+1	
	print(noOfObjectsInAClass)
	"""
	"""
	#train
	avgs=[]
	for i in range(len(train)):
	"""
	#print(avgs.columns)


	#test
	#avgs = pd.DataFrame(data=avgs)

	avgs=pd.read_csv("avgs.csv")

	score=0	
	classes = []
	for j in range(len(test.columns)):
		distances=[]
		for i in range(len(avgs.columns)):
			#print(np.sqrt(np.sum(np.square(test.iloc[:,0]-train.iloc[:,i]))))
			distances.append(np.sqrt(np.sum(np.square(test.iloc[:,j]-avgs.iloc[:,i]))))
		#print(min(distances))
		#print(np.argmin(distances))
		#print(int(float(avgs.columns[np.argmin(distances)])),",",int(float(test.columns[j])))
		minDistanceFromClass=int(float(avgs.columns[np.argmin(distances)]))
		if minDistanceFromClass==int(float(test.columns[j])):
			classes.append(minDistanceFromClass)
			score=score+1
	print()
	print("Classes correctly predicted (Centroid): ", score)
	score=score/len(test.columns)
	return (score, classes)

