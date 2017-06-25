#kaggle的泰坦尼克号幸存者预测，用的是决策树模型预测

import pandas as pd
import numpy as np

train_data=pd.read_csv("C:\\Users\\10132\\Downloads\\train.csv")
test_data=pd.read_csv("C:\\Users\\10132\\Downloads\\test.csv")

#特征选取
train_x=train_data[['Pclass','Age','Sex']]
train_y=train_data[['Survived']]


test_x=test_data[['Pclass','Age','Sex']]

#把Age中的缺失值用平均数替换，还可以选择众数，中位数或者直接将缺省作为一类
train_x['Age'].fillna(train_x['Age'].mean(),inplace=True)
test_x['Age'].fillna(test_x['Age'].mean(),inplace=True)

from sklearn.feature_extraction import DictVectorizer
vec=DictVectorizer()

train_x=vec.fit_transform(train_x.to_dict(orient='record'))
test_x=vec.fit_transform(test_x.to_dict(orient='record'))

from sklearn.tree import DecisionTreeClassifier
#决策树分类器
dtc=DecisionTreeClassifier()
dtc.fit(train_x,train_y)

prediction=dtc.predict(test_x)

dict={}
dict['PassengerId']=test_data['PassengerId'][:]
dict['Survived']=prediction

dataframe=pd.DataFrame(dict)

#保存数据
dataframe.to_csv("result.csv",index=False,sep=' ')



