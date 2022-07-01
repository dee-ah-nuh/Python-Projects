# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:57:31 2022

@author: Diana Valladares
"""
from httplib2 import Http
import webbrowser
import os
import time
# Automating Desk Set Up at Work
# Openinig the first tab which is Trello

url =['https://trello.com/b/UlJBIX0I/diana-valladares-project-status', 'https://docs.google.com/presentation/d/1OizQel4Dn8H5RJ0EYq_G19iWHbnxph2Pxl8qnaPfRR4/edit#slide=id.gee86c2a8b6_0_0', 
     'https://docs.google.com/spreadsheets/d/1kaMbk37Hg2nJ7PVkItM_KBYTcW0JrnIukrzpbsZIkfo/edit#gid=1581742535', 'https://mail.google.com/mail/u/0/?ogbl#inbox/FMfcgzGpGnFnJdvMrxKPdJrtCBjQVrpq',
     'https://us02web.zoom.us/account/report/user?from=06/28/2022&to=06/28/2022', 'https://app.close.com/tasks/inbox/']
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('C:/Program Files/Google/Chrome/Application/chrome.exe'))

def run():
    for i in range(len(url)):
        webbrowser.get('chrome').open(url[i])
        
run()
print(...and have a nice day!)


