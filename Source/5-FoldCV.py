import pandas as pd
import numpy as np
from DataHandler import pickDataClass
from DataHandler import splitData2TestTrain
from KNN import KNN
from Centroid import Centroid
from svm import SVM
#crossValidation
numberOfDataitemsInAClass=39
jump=int(numberOfDataitemsInAClass/5)
print(jump)
rangeStart=1
rangeEnd=int((rangeStart+jump)-1)
CVAvgKNN=0
CVAvgCentroid=0
CVAvgSVM=0
CVAvgLR=0

for k in range(0,5):
	rangeTotal=str(rangeStart) + ":" + str(rangeEnd)
	print()
	print("Test range -> ",rangeStart,":",rangeEnd)
	splitData2TestTrain("pickedClasses.csv",numberOfDataitemsInAClass,rangeTotal)
	#print()

	#print
	train = pd.read_csv("train.csv")
	test = pd.read_csv("test.csv")
	print()
	score=KNN(train,test)
	print()
	CVAvgKNN=CVAvgKNN+score

	score=Centroid(train,test)
	CVAvgCentroid= CVAvgCentroid + score
	
	score=SVM(train,test)
	CVAvgSVM=CVAvgSVM + score

	rangeStart=rangeEnd+1
	rangeEnd=(rangeStart+jump)-1	

print()
print("*************************************")
print("Average 5-fold CV KNN score: ", CVAvgKNN/5, "/1.0")
print("*************************************")

print()
print("*************************************")
print("Average 5-fold CV Centroid score: ", CVAvgCentroid/5, "/1.0")
print("*************************************")

print()
print("*************************************")
print("Average 5-fold CV SVM score: ", CVAvgSVM/5, "/1.0")
print("*************************************")

