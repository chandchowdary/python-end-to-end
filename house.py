import numpy as np
import pandas as pd
df = pd.read_csv("C:/Users/18162/Desktop/machine learning/house-prices-advanced-regression-techniques/train.csv")
features = ["MSSubClass","LotFrontage","LotArea","OverallQual","OverallCond","YearBuilt","YearRemodAdd","Condition1",
            "ExterQual","BsmtFinSF1","BsmtFinSF2","BsmtUnfSF","TotalBsmtSF","1stFlrSF","2ndFlrSF","LandContour","GrLivArea",
            "BsmtFullBath","BsmtHalfBath","FullBath","HalfBath","BedroomAbvGr","KitchenAbvGr","TotRmsAbvGrd","Neighborhood","GarageYrBlt",
            "GarageCars","GarageArea","SaleCondition","OpenPorchSF","EnclosedPorch","3SsnPorch","RoofStyle","SaleType","MiscVal","MoSold","YrSold"]
##weights = [1]*80
train_x = df[features]
train_x = pd.get_dummies(train_x)
train_y = df.SalePrice
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
imputer.fit(train_x)
train_x = imputer.transform(train_x)
##train_x = weights * train_x
from sklearn.preprocessing import *
scaler = MinMaxScaler()
scaler.fit(train_x)
train_x = scaler.transform(train_x)
from sklearn.linear_model import LogisticRegression
classifierLR = LogisticRegression()
classifierLR.fit(train_x,train_y)
df = pd.read_csv("C:/Users/18162/Desktop/machine learning/house-prices-advanced-regression-techniques/test.csv")
test_x = df[features]
test_x = pd.get_dummies(test_x)
test_x = imputer.transform(test_x)
test_x = scaler.transform(test_x)
pred_y = classifierLR.predict(test_x)
##train_x = weights * test_x
test = df.Id
output = pd.DataFrame({'Id':test[0:],'SalePrice':pred_y[0:]})
output.to_csv("C:/Users/18162/Desktop/machine learning/house-prices-advanced-regression-techniques/output.csv",index=False) 

