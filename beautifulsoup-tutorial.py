# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 08:45:22 2022

@author: BEEMO
"""

import pandas as pd, numpy as np
import regex
import requests 

print("# ============================================================================================")
print("#Beautiful Soup Tutorial")
print("# ============================================================================================")
from bs4 import BeautifulSoup as bs
import requests 
#installing both libraries and modules
# google_page = requests.get("https://www.google.com/")
# #print(google_page.status_code)
# #i printed the status code because if 200 then its actually correct and content = present
# #if it gives you like 404 error content is not present
# #print(google_page.headers)
# #these are all the headers encrypted within the google page as JSON
# src = google_page.content
# #print(src)
# soup = BeautifulSoup(src, "lxml")
# #created a links variables that is going to output all the links that 
# #share and include the string character "a"
# links = soup.find_all("a")
#print(links,'\n\n')


"""STEPS to FOLLOW Web Scraping"""
#0. If not done so, (if chrome) enable: chrome://flags/#allow-insecure-localhost as the local host server on computer

#1. load webpage with requests

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

#2. print content

soup = bs(r.content, 'lxml')

#3. convert to bs object


print(soup.prettify())

"""HTML version of the webpage"""
#grabbing any header with find and find_all
first_header = soup.find("h2")
#prints the first header and stops on first element
headers = soup.find_all("h2")
#creates a list of all h2 elements
##passing a list of elements to look for
first_header = soup.find(['h1', 'h2'])
headers = soup.find_all(['h1', 'h2'])
##passing attributes in a find/find_all function
paragraph = soup.find_all("p")
#we can nest find and find_all calls
body = soup.find("body")
#narrows down where we scrapping from if we have a massive page 
div = body.find('div')
#header in the div
header = div.find("h1")
#we can search for specific strings in this case:
    #paragraphs with the words "SOME"
string_search = soup.find_all("p")
#it gives us nothing because it actually looks for the specific phrase;
#if we have the specific phrase then we can leverage it to find precise words
string_search = soup.find_all("p", string ="Some bold text")
#aha!
#we import regex library to find just some of the words

import regex as re
#lets try string search again
string_search = soup.find_all("p", string = re.compile('Some'))
#some words have different capitalizations :
    #take headers for example
headers = soup.find_all("h2", string = re.compile("(H|h)eader"))


"""CSS version of the webpage"""
#exactly the same as the find/find_all libraries
# content = soup.find_all("h1")
content = soup.select("h1")
#if we want to find the body
body = soup.body
content = soup.select("div p")
#getting the paragraphs directly after h2 
paragraphs = soup.select("h2 ~ p")
#if we want to grab the bold text after the paragraph with paragraph-id: "paragraph-id"
# </h2>
# <p id="paragraph-id">
#  <b>
#   Some bold text
boldtext = soup.select("p#paragraph-id b")
#running nested calls - direct descendants of the body
#it would return paragraphs within the same indentation as the body
paragraphs = soup.select("body > p")
# we iterate through the list to print out the italisized text items
#for paragraph in paragraphs:
   # print(paragraph.select("i"))
    
    
    
"""Getting HTML Properties"""
header = soup.find("h2")
div = soup.find('div')
#if theres multiple chuildren within the object (options), get text returns all the optins
#.find will retun non
div.get_text()
link =soup.find("a")
link['href']
paragraphs = soup.select("p#paragraph-id")
#this will spit out: the id from the first paragraph
paragraphs[0]['id']


"""Code Navigation"""
###PATH SYNTAX###
soup.body.div.h1.string
#####                        Terms:

# =============================================================================
#  <head>
#   <title>
#    HTML Example
#   </title>
#  </head>
#  <body>
#   <div align="middle">
#    <h1>
#     HTML Webpage
#    </h1>
#    <p>
#     Link to more interesting example:
#     <a href="https://keithgalli.github.io/web-scraping/webpage.html">
#      keithgalli.github.io/web-scraping/webpage.html
#     </a>
#    </p>
#   </div>
# =============================================================================
dTerms = {

 "Parent": "in this case, body is the parent of div" ,
"Sibling": "head and body are siblings since they fall within the same identation " ,
"Child": "div is the child of the body"
}

soup.body.find("div").find_next_siblings()

print("# ========================================================================")
print("#Beautiful Soup - Task 1 - Specific Links")
print("# ========================================================================")

#1 Load the webpage
keith = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
#2 make bs into an object 
src = keith.content
#3 make soup an object/class
soup = bs(src, "lxml")


#task 1 - grab all the social links from the webpage
# <ul class="socials">
#  <li class="social instagram">
#   <b>
#    Instagram:
#   </b>
#   <a href="https://www.instagram.com/keithgalli/">
#    https://www.instagram.com/keithgalli/
#   </a>
#  </li>
#  <li class="social twitter">
#   <b>
#    Twitter:
#   </b>
#   <a href="https://twitter.com/keithgalli">
#    https://twitter.com/keithgalli
#   </a>
#  </li>
#  <li class="social linkedin">
#   <b>
#    LinkedIn:
#   </b>
#   <a href="https://www.linkedin.com/in/keithgalli/">
#    https://www.linkedin.com/in/keithgalli/
#   </a>
#  </li>
#  <li class="social tiktok">
#   <a href="https://www.tiktok.com/@keithgalli">
#    https://www.tiktok.com/@keithgalli

    
social_links = soup.select("a")

socials = soup.find_all("a")

#option 1
socials = [[soup.find_all("a", string = re.compile("instagram")) + 
soup.find_all("a", string = re.compile("tiktok")) + 
soup.find_all("a", string = re.compile("linkedin")) + 
soup.find_all("a", string = re.compile("twitter"))]]

# . is for the class names //  # is for the id in paragraphs
socialmedia  = soup.select("ul.socials")
#out: 
 #[<ul class="socials">
 # <li class="social instagram"><b>Instagram: </b><a href="https://www.instagram.com/keithgalli/">https://www.instagram.com/keithgalli/</a></li>
 # <li class="social twitter"><b>Twitter: </b><a href="https://twitter.com/keithgalli">https://twitter.com/keithgalli</a></li>
 # <li class="social linkedin"><b>LinkedIn: </b><a href="https://www.linkedin.com/in/keithgalli/">https://www.linkedin.com/in/keithgalli/</a></li>
 # <li class="social tiktok"><b>TikTok: </b><a href="https://www.tiktok.com/@keithgalli">https://www.tiktok.com/@keithgalli</a></li>


socialmedia = soup.select("ul.socials a")

#out: 
 #[<a href="https://www.instagram.com/keithgalli/">https://www.instagram.com/keithgalli/</a>,
 #<a href="https://twitter.com/keithgalli">https://twitter.com/keithgalli</a>,
 #<a href="https://www.linkedin.com/in/keithgalli/">https://www.linkedin.com/in/keithgalli/</a>,
 #<a href="https://www.tiktok.com/@keithgalli">https://www.tiktok.com/@keithgalli</a>]


#only the a tags (hint hint ['href'])
actualsociallinks = [link['href'] for link in socialmedia]

# ['https://www.instagram.com/keithgalli/',
#  'https://twitter.com/keithgalli',
#  'https://www.linkedin.com/in/keithgalli/',
#  'https://www.tiktok.com/@keithgalli']

#option 2
#using find all

ulist = soup.find("ul", attrs= {"class": 'socials'})
# <ul class="socials">
# <li class="social instagram"><b>Instagram: </b><a href="https://www.instagram.com/keithgalli/">https://www.instagram.com/keithgalli/</a></li>
# <li class="social twitter"><b>Twitter: </b><a href="https://twitter.com/keithgalli">https://twitter.com/keithgalli</a></li>
# <li class="social linkedin"><b>LinkedIn: </b><a href="https://www.linkedin.com/in/keithgalli/">https://www.linkedin.com/in/keithgalli/</a></li>
# <li class="social tiktok"><b>TikTok: </b><a href="https://www.tiktok.com/@keithgalli">https://www.tiktok.com/@keithgalli</a></li>
# </ul>

links = ulist.find_all("a")


actual = [link['href'] for link in links]
# ['https://www.instagram.com/keithgalli/',
#  'https://twitter.com/keithgalli',
#  'https://www.linkedin.com/in/keithgalli/',
#  'https://www.tiktok.com/@keithgalli']

#option 3
lists = soup.select("li.social a")

thirdoption = [link['href'] for link in lists]


print("# ========================================================================")
print("#Beautiful Soup - Task 2 - Table")
print("# ========================================================================")

#task 2 making the table a pandas dataframe
#grabbing the information from the table
table = soup.select("table.hockey-stats")[0]



###PSEUDO CODE FOR TABLE
#
# l =[]
# for tr in table_rows:
#   td = tr.find_all('td')
#   row = tr.text for tr in td
#   l.append(row)
#   pd.DataFrame(l, columns=["A", "B", ...])
#
#
#grab all table heads first
columns = table.find("thead").find_all("th")
# out:
# [<th class="season" data-sort="">S</th>,
#  <th class="team" data-sort="team">Team</th>,
#  <th class="league" data-sort="league">League</th>,
#  <th class="regular gp" data-sort="gp">GP</th>,
#  <th class="regular g" data-sort="g">G</th>,
#  <th class="regular a" data-sort="a">A</th>,
#  <th class="regular tp" data-sort="tp">TP</th>,
#  <th class="regular pim" data-sort="pim">PIM</th>,
#  <th class="regular pm" data-sort="pm">+/-</th>,
#  <th class="separator"> </th>,
#  <th class="postseason">POST</th>,
#  <th class="postseason gp" data-sort="playoffs-gp">GP</th>,
#  <th class="postseason g" data-sort="playoffs-g">G</th>,
#  <th class="postseason a" data-sort="playoffs-a">A</th>,
#  <th class="postseason tp" data-sort="playoffs-tp">TP</th>,
#  <th class="postseason pim" data-sort="playoffs-pim">PIM</th>,
#  <th class="postseason pm" data-sort="playoffs-pm">+/-</th>]
column_names = [c.string for c in columns]
# out:
# ['S',
#  'Team',
#  'League',
#  'GP',
#  'G',
#  'A',
#  'TP',
#  'PIM',
#  '+/-',
#  '\xa0',
#  'POST',
#  'GP',
#  'G',
#  'A',
#  'TP',
#  'PIM',
#  '+/-']

#making a dataframe with an html table

rows = table.find("tbody").find_all("tr")
l = []
for tr in rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

dfmit = pd.DataFrame(l, columns=column_names)

dfmit.loc[dfmit['Team'] != "Did not play"]

#eliminates all empty columns with no values  

# =============================================================================
nan_value = float("NaN")
dfmit.replace("", nan_value, inplace=True)
dfmit.dropna(how='all', axis=1, inplace=True)
# ========================================================================

#changing the empty column name 
dfmit.columns.values[9] = 'Lines'



print("# ========================================================================")
print("#Beautiful Soup - Task 3 - Making a list with a specific word")
print("# ========================================================================")
#grabbing all the fin facts that have the word "is"

funfact = soup.select("ul.fun-facts li")
facts_with_is = [fact.find(string=re.compile("is")) for fact in funfact]
#gets rid of the none
#facts_with_is = [fact for fact in facts_with_is if fact]
facts_with_is = [fact.find_parent().get_text() for fact in facts_with_is if fact]



print("# ========================================================================")
print("#Beautiful Soup - Task 4 - Downloading images")
print("# ========================================================================")


# Load the webpage content
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url+"webpage.html")

# Convert to a beautiful soup object
soup = bs(r.content, "lxml")

images = soup.select("div.row div.column img")
image_url = images[0]['src']
full_url = url + image_url

img_data = requests.get(full_url).content
with open('Como.jpg', 'wb') as handler:
    handler.write(img_data)



#mystery challenge -solve 

#paragraph tags
#id = "secret-words"


#load content - (i modified the import page so it would not 
                    #give me any more connection errors)
#make soup an object
#begin scrapping


test_link = "https://keithgalli.github.io/web-scraping/webpage.html"
headers ={
    "User-Agent": "Chrome",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}


r = requests.get(test_link, headers=headers)
soup = bs(r.content, "lxml")



files = soup.select("div.block a")

relative_files = [f['href'] for f in files]


url = "https://keithgalli.github.io/web-scraping/"
for f in relative_files:
  full_url = url + f
  page = requests.get(full_url)
  bs_page = bs(page.content)
  secret_word_element = bs_page.find("p", attrs={"id": "secret-word"})
  secret_word = secret_word_element.string
  print(secret_word)



















