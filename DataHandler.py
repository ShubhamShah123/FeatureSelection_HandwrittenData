import warnings
warnings.filterwarnings("ignore")

def pickDataClass(filename,class_IDs):
	import pandas as pd
	import numpy as np
	dataset = pd.read_csv(filename)
	#class_IDs=[1,2,5]
	#print(class_IDs)
	no_of_items_per_class=39
	c=0
	#print("**************")
	index=0
	X=[]
	for j in class_IDs:
		X += no_of_items_per_class*[j]
	
	indexX=0
	for i in class_IDs:
		c=(i-1)*no_of_items_per_class
		if indexX==0:
			XData=dataset.iloc[:,c:c+no_of_items_per_class].values
			indexX=indexX+1		
		else:
			Xx=dataset.iloc[:,c:c+no_of_items_per_class].values
			XData=np.concatenate((XData,Xx),axis=1)
	X=np.vstack([X,XData]) 	
	np.savetxt("pickedClasses_exam.csv",X, fmt='%i',delimiter=',', newline='\n')
	print()

def splitData2TestTrain(filename,no_of_items_per_class,test_instances):
	import pandas as pd
	import numpy as np
	X=[]
	#no_of_items_per_class=10
	#filename="try.csv"
	dataset = pd.read_csv(filename)

	#test_instances="3:5"
	testinstances=test_instances.split(":")

	testrangestart=int(testinstances[0])
	testrangeend=int(testinstances[1])

	no_of_classes=(len(dataset.columns)/no_of_items_per_class)
	no_of_classes=int(no_of_classes)

	testLabels=[]
	trainLabels=[]

	#labeling
	noOfTests=(testrangeend-testrangestart)+1
	noOfTrain=no_of_items_per_class-noOfTests
	print()
	print("No. of train: ",noOfTrain,"*", no_of_classes)
	print("No. of tests: ",noOfTests,"*", no_of_classes)
	print()
	for j in range(0,len(dataset.columns),no_of_items_per_class):
		for i in range(0,noOfTests):
			testLabels.append(dataset.columns[j])
		for k in range(0,noOfTrain):
			trainLabels.append(dataset.columns[j])

	testLabels = [int(float(testLabels)) for testLabels in testLabels]
	#print(testLabels)
	trainLabels = [int(float(trainLabels)) for trainLabels in trainLabels]
	#print(trainLabels)

	index=0
	for i in range(1,no_of_classes+1):
		startOfClass=(no_of_items_per_class)* (i-1)
		if index==0:		
			test=dataset.iloc[:,(startOfClass) + (testrangestart-1):(startOfClass) + (testrangeend)]
			index=index+1
			train=dataset.iloc[:,startOfClass:(startOfClass) + (testrangestart-1)]
			train2=dataset.iloc[:,(startOfClass) + (testrangeend):(startOfClass) + no_of_items_per_class]
			train=np.concatenate((train,train2),axis=1)
		else:
			testTemp=dataset.iloc[:,(startOfClass) + (testrangestart-1):(startOfClass) + (testrangeend)]
			test=np.concatenate((test,testTemp),axis=1)

			tempTrain=dataset.iloc[:,startOfClass:(startOfClass) + (testrangestart-1)]
			train2=dataset.iloc[:,(startOfClass) + (testrangeend):(startOfClass) + no_of_items_per_class]
			tempTrain=np.concatenate((tempTrain,train2),axis=1)
			train=np.concatenate((train,tempTrain),axis=1)

	test=np.vstack([testLabels,test])
	train=np.vstack([trainLabels,train])
	np.savetxt("test_exam.csv",test, fmt='%i',delimiter=',', newline='\n')
	np.savetxt("train_exam.csv",train, fmt='%i',delimiter=',', newline='\n')
	return (train,test)

	#for i in dataset.columns:
	#	Test+=

	"""
	TestLabels=[]
	#for i in range(testrangestart,testrangeend):
	#	TestLabels+=no_of_items_per_class*[i]

	testrangestart=testrangestart-1
	testrangeend=testrangeend-1

	#R=dataset.iloc[0,testrangestart:testrangeend*no_of_items_per_class]

	#print(R)

	#TestData
	print(testrangestart)
	print(testrangeend)

	X=dataset.iloc[:,testrangestart:testrangeend*no_of_items_per_class]

	print(X)


	#testrangeend=testrangeend+2
	#testrangestart=testrangestart+1



	#Y=dataset.loc[:,dataset.columns<str(testrangestart)].values
	#Z=dataset.loc[:,dataset.columns>str(testrangeend)].values

	Y=dataset.iloc[:,:testrangestart*no_of_items_per_class]
	Z=dataset.iloc[:,testrangeend*no_of_items_per_class:]

	#print (Y)

	#Shehzad

	for i in dataset.columns:
		print(float(i))
		print(float(i)>2)

	# print(dataset.columns)
	# print(dataset.columns >= "4")

	k=0.0
	highrange=0.0
	for i in dataset.columns:
		k=float(i)
		if k >= float(testrangeend):
			highrange=k
	Z=dataset.iloc[:,highrange:testrangeend*no_of_items_per_class]
	###


	u=dataset.columns

	print(pd.isin(u, "1"))

	#Z=dataset.loc[:,dataset.columns>"30"]


	Y=np.concatenate((Y,Z),axis=1)

	#Y=pd.concat([Y,Z], axis=1)

	#Y=Y.loc[:,Y.columns>=testinstances[1]]
	#pd.set_option('display.max_columns', 10000)
	#print(dataset.columns)
	#print(Y)
	print(type(Y))
	np.savetxt("train.csv",Y, fmt='%i',delimiter=',', newline='\n')

	#Y.to_csv("train2.csv",index='true')






	#np.savetxt("trainsplit.csv",X, fmt='%i',delimiter=',', newline='\n')


	for i in dataset:	
		if float(i)>=testrangestart and float(i)<=testrangeend:
			#This is the testing datasetta
			print(dataset.loc[:,i])
		else:
			print("Train")
			#This is the training data 
	#for j in range(testinstances[0],testinstances[1]):
	#		X += no_of_items_per_class*[j]
	"""
def letter_2_digit_convert(letters):
	#letters=['a','B','d','E']

	integers=[]
	for i in letters:
		if i.isupper():
			#print(ord(i)-64)
			integers.append(ord(i)-64)
		else:
			#print(ord(i)-96)
			integers.append(ord(i)-96)

	#print(integers)
	return integers
	"""
	import matplotlib.pyplot as plt
	plt.plot([1,2,3,4])
	plt.ylabel('some numbers')
	plt.show()
	"""



