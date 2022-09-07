# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:54:44 2022

@author: Diana Valladares
"""
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import json

with open("C:/Users/Diana Valladares/Documents/GitHub/Python-Projects/exported-zaps-2022-07-26T21_49_13.418Z.json") as zapier_file:
    df=json.load(zapier_file)


df2 = json_normalize(df, 'zaps')
print(df2)

df2.dropna()
print(df2)

MKT3 = df2['title'].value_counts()
print(MKT3)
