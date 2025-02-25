# -*- coding: utf-8 -*-
"""Hill&ValleyPrediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z1me1kK2qJzUgn5vnq_TcwhUp3pfJtbG

**Hill and Valley Prediction using Logistic Regression**

*Objective :* To create a machine learning model using logistic regression to accurately predict whether a given terrain is a hill or a valley. This project involves data preprocessing, training the model, and evaluating its performance to ensure reliable predictions. The goal is to develop a practical tool for applications in fields like geography and environmental studies.

*Data Source:* https://github.com/YBIFoundation/Dataset/raw/main/Hill%20Valley%20Dataset.csv

# Import Libraries
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

"""# Import Data"""

df=pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Hill%20Valley%20Dataset.csv')

"""# Describing Data

Get The First Five Rows of Dataframe
"""

df.head()

""" Get Information of Dataframe"""

df.info()

"""Get the Summary Statistics"""

df.describe()

"""Get Column Names"""

df.columns

print(df.columns.tolist())

""" Get Shape of Dataframe"""

df.shape

"""Get Unique Values in y Variable"""

df['Class'].value_counts()

df.groupby('Class').mean ()

"""# Define Target Variable (y) and Feature Variables (X)"""

y= df['Class']

y.shape

y

X = df.drop('Class', axis=1)

X.shape

X

"""# Data Visualisation"""

plt.plot(X.iloc[0,:])
plt.title('Valley');

plt.plot(X.iloc[1,:])
plt.title('Hill');

"""# Data Preprocessing"""

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

X = ss.fit_transform(X)

X

X.shape

"""# Train Test Split"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2529)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""# Modeling"""

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(X_train, y_train)

"""# Model Prediction"""

y_pred = lr.predict(X_test)

y_pred.shape

y_pred

"""Probability of each predicted class"""

lr.predict_proba(X_test)

"""# Evaluation"""

from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

"""# Future Predictions"""

X_new = df.sample(1)

X_new

X_new.shape

X_new = X_new.drop('Class', axis=1)

X_new

X_new.shape

X_new = ss.fit_transform(X_new)

y_pred_new = lr.predict(X_new)

y_pred_new

lr.predict_proba(X_new)

"""# Explanation
In this project, a logistic regression model was successfully implemented to predict whether a terrain feature is a hill or a valley based on the provided dataset. The model achieved a respectable accuracy, demonstrating its potential for practical applications in fields like geography and environmental studies. Key steps included data preprocessing, model training, and evaluation using metrics such as accuracy and confusion matrix. Future improvements could involve hyperparameter tuning and incorporating additional features to further enhance the model's performance.
"""