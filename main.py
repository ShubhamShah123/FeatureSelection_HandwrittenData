from DataHandler import pickDataClass
from DataHandler import splitData2TestTrain
from DataHandler import letter_2_digit_convert
from Source.KNN import KNN
from Source.Centroid import Centroid
from Source.SVM import SVM

import pandas as pd
import numpy as np

#Task A:
name = input("Enter your name: ")
print("\nName: ",name)
f_name, l_name = name.split()
name_chnge = f_name[-4:] + l_name[-4:]
name = list(name_chnge)
print("Classes: ",name)
input_name = ''.join(name)
pickDataClass("Source/HandWrittenLetters.csv",letter_2_digit_convert(input_name))
trainData, testData=splitData2TestTrain("pickedClasses_exam.csv",39,"20:39")
train = pd.read_csv("train_exam.csv")
test = pd.read_csv("test_exam.csv")
print("\ntrain_exam.csv and test_exam.csv files created\n")

knn_score, knn_classes = KNN(train,test,3)
KNN_CLASS = []
for i in knn_classes:
	KNN_CLASS.append(chr(int(i) + 64))
print("\n--- KNN Class Labels : ---\n\n",KNN_CLASS)
print("\n--- KNN: SCORE -> {0} ---",knn_score)

knn_score, knn_classes = KNN(train,test,5)
KNN_CLASS = []
for i in knn_classes:
	KNN_CLASS.append(chr(int(i) + 64))
print("\n--- KNN Class Labels : ---\n\n",KNN_CLASS)
print("\n--- KNN: SCORE -> {0} ---".format(knn_score))


centroid_score, centroid_classes = Centroid(train,test)
Centroid_CLASS = []
for i in centroid_classes:
	Centroid_CLASS.append(chr(int(i) + 64))
print("\n--- Centroid Class Labels : ---\n\n",Centroid_CLASS)
print("\n--- Centroid: SCORE -> {0}% ---".format(centroid_score*100))

svm_score, svm_classes = SVM(train,test)
SVM_CLASS = []
for i in svm_classes:
	SVM_CLASS.append(chr(int(float(i)) + 64))
print("\n--- SVM Class Labels : ---\n\n",SVM_CLASS)
print("\n--- SVM: SCORE -> {0}% ---".format(svm_score*100))
