# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:32:54 2022

@author: Diana Valladares
"""

import json 
import pandas as pd
import numpy as np

fileSon = open("C:/Users/Diana Valladares/Downloads/exported-zap-2022-07-18T15_30_59.414Z.json")

df= json.load(fileSon)

for i in df['zaps']:
    print(i)
    
      