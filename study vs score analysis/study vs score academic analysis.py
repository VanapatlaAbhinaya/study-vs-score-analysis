#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#reading csv file using head and tail functions
df =pd.read_csv("archive.zip")
df.info()
df.head()
df.tail()
#checking null values
print(df.isnull().sum())
#splitting dataset into train and set
x=df.iloc[:,0:1]
y=df.iloc[:,1:]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=1/4, random_state=0)
x_train
y_train
from sklearn.preprocessing import StandardScaler
sc =StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
print(x_train)
#linear regresion model
from sklearn.linear_model import LinearRegression
r=LinearRegression()
r.fit(x_train,y_train)
y_predict=r.predict(x_test)
print(y_predict)
plt.scatter(x_train, y_train, color = "red")
plt.plot(x_train, r.predict(x_train), color = "green")
plt.title("hrs and per ")
plt.xlabel("hrs")
plt.ylabel("per")
plt.show()
h=[[6.5]]
r.predict(h)
print(h)

print(r.coef_)
print(r.intercept_)
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
print(r.score(x_test,y_test))

