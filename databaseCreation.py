# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 12:40:21 2022

@author: BEEMO
"""
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import json

pymysql.install_as_MySQLdb()
# =============================================================================
# Connecting the database to the database credentials file
# =============================================================================
with open("/Users/BEEMO/.secret/mysql.json") as f:
    login = json.load(f)
login.keys()
# =============================================================================
# Connection to the database dashboard
# =============================================================================
connection_str  = f"mysql+pymysql://{login['username']}:{login['password']}@localhost:3307/"
engine = create_engine(connection_str)

# =============================================================================
# # create a database 
# 
# q = ''' CREATE DATABASE dataBaseName '''
# 
# # delete a database 
# 
# q = ''' DROP DATABASE dataBaseName '''

# # show all the tables
# 
# q = '''SHOW TABLES '''  
# =============================================================================

q = '''CREATE DATABASE footballDatabase'''
databasecreation = pd.read_sql(q, engine)

