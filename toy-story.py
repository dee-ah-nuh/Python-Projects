# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 16:22:45 2022

@author: BEEMO
"""

from bs4 import BeautifulSoup as bs
import requests

#load page
#soup as object
#print html 

r = requests.get("https://en.wikipedia.org/wiki/Toy_Story_3")
# or soup = bs(r.content)
src = r.content
soup = bs(src, "lxml")


info_box = soup.find_all("table", {"class": "infobox vevent"})

info_box = soup.find_all("table", {"class": "infobox vevent"})











print(soup.prettify())