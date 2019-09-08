import numpy as np
import pandas as pd

features = ["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
weights = [5,1,1,1,1,10,10,1,1,1]
##weights = [1] * 10

df = pd.read_csv("C:/Users/18162/Desktop/machine learning/train.csv")
train_X = df[ features ]
train_Y = df.Survived

# handle qualitative predictors
train_X = pd.get_dummies(train_X)
train_X.info()

# handle missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
imputer.fit(train_X)
train_X = imputer.transform(train_X)

# normalize the scales
from sklearn.preprocessing import *  
##scaler = StandardScaler()
scaler = MinMaxScaler()
scaler.fit(train_X)
train_X = scaler.transform(train_X)

# assign weights
train_X = weights * train_X

#print(train_X)

# various classifiers
from sklearn.neighbors import KNeighborsClassifier  
classifier = KNeighborsClassifier(n_neighbors=5)
##
##from sklearn.linear_model import LogisticRegression
##classifier = LogisticRegression()

##
##from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
##classifier = LinearDiscriminantAnalysis()
##
##from sklearn.tree import DecisionTreeClassifier
##classifier = DecisionTreeClassifier(criterion="entropy",max_depth=4)
####
##from sklearn.ensemble import BaggingClassifier 
##classifier = BaggingClassifier(KNeighborsClassifier(),max_samples=0.5,max_features=0.5)
##classifier = BaggingClassifier(n_estimators=20)
##from sklearn.ensemble import RandomForestClassifier
##classifier = RandomForestClassifier(n_estimators=100,max_depth=2,random_state=0)
##classifier = RandomForestClassifier(min_samples_split=0.10,n_estimators=100)


# training
classifier.fit(train_X, train_Y)
##pred_X=classifier.predict(weights*train_X)

df = pd.read_csv("C:/Users/18162/Desktop/machine learning/test.csv")
test_X = df[ features ]
test_X = pd.get_dummies(test_X)
test_X = imputer.transform(test_X)
test_X = scaler.transform(test_X)
test_X = weights * test_X
test_S=df.PassengerId

pred_Y = classifier.predict(test_X)
print(pred_Y)

##################################################
## Write the prediction result to a csv file below
##################################################
f=open("survival.csv","w")
f.write("PassengerId,Survived\n")
for i in range(len(pred_Y)):
     f.write("{},{}\n".format(test_S[i],pred_Y[i]))
f.close()




