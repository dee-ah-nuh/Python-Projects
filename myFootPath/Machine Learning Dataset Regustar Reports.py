# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:06:46 2022

@author: Diana Valladares
"""

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
# Gave the enrolled dataset a name and initialized it
enrolled = pd.read_csv('C:/Users/Diana Valladares/Downloads/Group_Enrolled-2022-06-30 06-04-04 AM.csv')
enrolled.head()
print(enrolled)

print(enrolled.info())
#Wanted to see in depth the values of the dataset
active_students_values = enrolled['Active_Student'].value_counts()
print(enrolled['Active_Student'])
#Initialized and gave the unenrolled student dataset a name 
unenrolled = pd.read_csv('C:/Users/Diana Valladares/Downloads/Group_NotEnrolled-2022-06-29 06-04-02 AM.csv')
unenrolled.head()
print(unenrolled.head())
print(unenrolled.info())

#We begin Machine Learning by splitting  our datsets into training and testing
dropped_enroll = enrolled.drop(columns=['Class_Number', 'CLASS', 'Class_Descr', 'Enrollment_Drop_Date','First_Term_Eligible_To_Enroll'])
X= dropped_enroll
print(X.info())

#We create a pipeline to codify all those object feaures into integers and float numbers


from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr_pipe = 