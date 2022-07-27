# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:41:24 2022

@author: Diana Valladares
"""

from apiclient import discovery, errors
from httplib2 import Http
from oauth2client import file, tools
from oauth2client import  client as c
#from googleapiclient import errors
from datetime import datetime, timedelta
today=datetime.today().strftime('%Y-%m-%d')
from openpyxl import load_workbook, Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow #May be unneeded
# from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials
import re
import pandas as pd
#import numpy as np
import csv
import requests
import glob
import os.path
import time
import os
username=os.getlogin()
import gspread
import base64
#import email #may be unneeded
import webbrowser
#import csv
import json
#import closeio_api
import unidecode
from closeio_api import Client as CloseIO_API
#from requests.exceptions import ConnectionError
from email.mime.text import MIMEText
#import xlsxwriter
import traceback

ticY = time.perf_counter()


def get_emails():
    SCOPES = ['https://mail.google.com/']
    credentials_saapi_google = 
    client_saapi_google = 
    