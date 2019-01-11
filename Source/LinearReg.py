import numpy as np
import warnings

warnings.filterwarnings("ignore")

def LinearReg(trainData,testData):
	################################# SIMPLE LINEAR REGRESSION ###########################################3

	# Picking the dataclass

	############### FOR : HandWrittenLetters Dataset Use the following inputs ##################
	#dataset = dh.pickDataClass('HandWrittenLetters.csv', dh.letter_2_digit_convert('ABCDE'))
	#dataset = dh.pickDataClass('../../DataSets/HandWrittenLetters.txt', dh.letter_2_digit_convert('ABCDE'))
	#trainData, testData = dh.splitData2TestTrain('pickedClasses.csv', 39, '30:39')

	############### FOR : ATNT50 Dataset Use the following inputs ##################
	'''
	dataset = dh.pickDataClass('../../DataSets/ATNT50/trainDataXY.txt', [1,2,3,4])
	trainData, testData = dh.splitData2TestTrain('./try.csv', 10, '1:3')
	'''


	X_train=trainData[1:,:]
	y_train=trainData[0,:,None]
	X_test=testData[1:,:]
	y_test=testData[0,:]

	# Preprocessing 
	from sklearn.preprocessing import LabelEncoder, OneHotEncoder
	labelencoder_Y = LabelEncoder()
	y_train[:,0]=labelencoder_Y.fit_transform(y_train[:,0])
	onehotencoder=OneHotEncoder(categorical_features=[0])
	y_train=onehotencoder.fit_transform(y_train).toarray()
	y_train=y_train.transpose()

	# print("AFter labelencoder: \n",y_train)

	A_train=np.ones((1,len(X_train[0])))
	A_test=np.ones((1,len(y_test)))


	Xtrain_padding = np.row_stack((X_train,A_train))
	Xtest_padding = np.row_stack((X_test,A_test))

	B_padding = np.dot(np.linalg.pinv(Xtrain_padding.T), y_train.T)
	Ytest_padding = np.dot(B_padding.T,Xtest_padding)
	Ytest_padding_argmax = np.argmax(Ytest_padding,axis=0)+1
	err_test_padding = y_test - Ytest_padding_argmax
	TestingAccuracy_padding = (1-np.nonzero(err_test_padding)[0].size/len(err_test_padding))*100

	f=open('Regression_Output_Accuracy.txt','w')
	f.write('%.4f Percent'%TestingAccuracy_padding)
	f.close()
	#print(testData)
	score=0
	for j in range(len(testData[0])):
		if Ytest_padding_argmax[j] == testData[0][j]:
			score=score+1
	print()
	print("Classes correctly predicted (Linear Reg): ", score)
	score=score/len(testData[0])
	print("CV Linear Reg Score: ",score, "/1.0")
	#np.savetxt('Regression_Output.txt',Ytest_padding_argmax,fmt="%0.0f",delimiter=',')
	#print("Completed and output saved in [ Regression_Output.txt ] with accuracy in [ Regression_Output_Accuracy.txt ]")

	return score
