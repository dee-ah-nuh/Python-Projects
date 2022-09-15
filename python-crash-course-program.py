import pandas as pd
import numpy as np
# =============================================================================
# #first program
# =============================================================================
print('hello_world!')
#my name and some functions
name = "diana valladares"
print(name.title())
maxy= 'maxy'
maxy = maxy.title()
print(maxy)
print(maxy.upper())
print(name.lower())
#Using variables as strings 
#we firt initialize a variable, then wse the function notation in print
#finally we print the statement
fullname = f"{maxy}s owner's name  is {name}"
print(fullname)
print(f"i miss you {maxy}")
#lets do a function witihin a function i like to call it
#this program is gonna be so long, but well get there i swear
print(f"Hello, my name is {name.title()}, my favorite pet in the whole wide world is not Noma, its {maxy}")
print(f"{name} is about to start class")
#practicing f-strings
print(f'{maxy} is my fav dog, now that {name} is awake')
#Stripping Whitespace 
favorite_language = "python "
favorite_language.rstrip()
#stripping more whitespace
favorite_man = "my favorite person of all time is ethan, he is the very sweetest baby boy "
favorite_man.rstrip()
#okay so rstip just takes away the blank space at the end of the string
favorite_man.lstrip()
#lstrip takes
favorite_man.strip()
#a personal statement journal 
journal = "                i just learned something new today, i also think that ethan is the happiest rn with his new golf club lol             "  
print(journal.strip())
#ahhh the art of adding comments to better exlain yourself
#as if the code did not do that for us already LOL
print('\n\n\n')
# =============================================================================
# import this
# =============================================================================
print("the above is the import this by Tim Peters" ,"\n\n")
print("# =============================================================================")
print("# lists")
print("# =============================================================================")
#in order to represent a list we surround it by square brackets and string quotes
bicycle = ['wheels', 'rims', 'brakes' ]
print(bicycle)
#printing the list
print(bicycle[1].title())
#printing a selection within a list and making the first letter capitalized
print(bicycle[1][3].upper())
#print a selection of a list within a list
#firs it print out the word, then from that word it print out the \
#letter where we specify which character we want
print(bicycle[-1])
#chooses the last of the list
message = (f" omg! my bicycle's {bicycle[1].lower()} broke!").strip()
bicycle[0] = 'frame'
# if we refer to a position on a list as a variable it will replace it
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('ducati')
print(f'the following is a motorcycle: {motorcycles[1].title()}')
message2 = f"i havent had any motrocycles but i would love to have a\
    {motorcycles[2].title()}, cause theyre the best!"
print(message2)
#replacing and deleting - and modifying the previos list 
del motorcycles[0]
motorcycles[1] = 'bugatti'
motorcycles.append("tesla")
#.pop functions
popped_motor = motorcycles.pop()
# =============================================================================
# everytime we use the function .pop without specifying anything
# then the last item on the list is returned as well as the old list
# once that is returned and we print the list-tuple again, then we get
# the new list
# =============================================================================
last_owned = motorcycles.pop()
print(f"my last motorcycle was a {last_owned.lower()}, not really lol")

motorcycles.remove("yamaha")
motorcycles.append("yamaha")
motorcycles.append('trek')
motorcycles.append("specialized")
motorcycles.pop(0)
motorcycles.append("schwinn")
print(motorcycles)
# =============================================================================
# #creating a random dataframe 
# =============================================================================
#df = pd.DataFrame(np.random.randn(10000, 4), columns=list('ABCD'))

#Wedding List - Guests who cannot make it

wedding = []
wedding.append('mom')
wedding.append('dad')
wedding.append('sister')
wedding.append('ethans parents')
wedding.append('obama')
print('\n')
print(wedding.pop(3) + ' cannot make it')
wedding.append("ethans cousin peanut")
print('we have found a bigger table so we arew going to add more people:')
wedding.insert(3, 'ethans cousing Ramon')
wedding.remove('obama')
print(f" these are the following invitees: {wedding[4].title()}")

print("okay wtf, so i am only allwoed to invite two people, im sorry:")
wedding.pop()
wedding.pop()
wedding.remove('sister')
print(wedding)
#organizing a list
weed = ['indica', 'sativa', 'hybrid']
weed.sort()
weed.sort(reverse= True)
print('\n')
print(len(weed))
#SEEING THE WORLD
#before prooceeding some insight from Josh: "Always a dream, sometimes a nightmare, but never reality"
print('\n')
abroad = ['fiji', 'phillipines', 'melbourne', 'vietnam', 'singapore', 'cambodia']
print(sorted(abroad))
print(sorted(abroad, reverse=True))
abroad.sort()
abroad.sort(reverse=True)
print(len(wedding))
print("# =============================================================================")
print("# Loops and for loops")
print("# =============================================================================")
print('\n\n')
west = ['cowboys', 'bounty hunters', 'clint eastwood', 'gold rush', 'indians']
west.append('california')
print(west)

for west_tings in west:
    print(west_tings) 
    
for west_tings in west:
    print(f"i am a {west_tings.title()}, you can find me in california")    
    
deliveries = ['carol', 'patrick', 'diana valladares']
for deliveree in deliveries:
    print(f"\nthis bitch {deliveree.title()} got their package")
    print(f"{deliveree.lower()}, is one of the best folks ive ever delivered to""\n")
print("Im not crying, I just have something in my eye...")
    
print("\n")
for stuff in west:
    print(f"{stuff}, have/has been studied in the past and its really good to educate on these topics")
print("what do you say eh?")

pizzas = ['peperoni', 'meraguerita', 'mushrooms' , 'cheese', 'meat']
print("\nall my favorite pizza flavors are here! Look they have:")
for flavors in pizzas: 
    print(flavors)
print("i luv me sum za")
    

print("# =============================================================================")
print("# numerical lists with loops")
print("# =============================================================================")
for value in range( 678,700):
    print(f"\n{value}")
#in range is a funciton that print out a list of numbers when we assign the amount of numbers

even_numbers = list(range(36,51,5))
print(even_numbers)
print('\n')
squares = []
for value in range(210,310,10):
    square = value ** 2
    squares.append(square)
print(squares)
dogs = ['bc','gr', 'pb', 'ch']
for breed in dogs:
    print(breed)
print('\n')
myBday = []
for values in range(15,35,5):
    herbday = values * 2 
    myBday.append(herbday)
print(myBday)

print(min(myBday))
print(max(myBday))
print(sum(myBday)/2)
for values in range(1,21):
    print(f"this is the list of numbers: {values}")

#working with part of a list
ethans = ['dumb', 'broke', 'young', 'sweet', 'succsessful', 'thoughtful']
print(ethans[3])
for ethan in ethans:
    print(ethan)
print(ethans[:3])
print(ethans)

#slicing a list
print(ethans[2:])
print(ethans[-3:])

for personas in ethans:
    print(personas.title())
    
#the colon tells python its coipying a list
ethan = ethans[:]
print(ethan)
ethan.append("careless")
print(ethan)
for values in range(1,5):
    print(f"{values}")
    
print(values)
#prints last numnber on the list because it assigns the last variable as the variable values

print("# =============================================================================")
print("# tuples")
print("# =============================================================================")

house = (15, 5)
print(house)
print(f"the width of the house is: {house[1]}m")
print(f"the length of the house is: {house[0]}m")
for dimensions in house:
    print("\n", dimensions)
    
dimensions = (12,5)
for dimension in dimensions:
    print(dimension)
fast_food = ['mcdonalds', "bkg", "wendys", "subway"]
for food in fast_food:
    if food == "bkg":
        print('the king')
    else:
        print("other clowns")

fast_food = ['mcdonalds', "bkg", "wendys", "subway"]
requested_food = "mcdonalds"      
if requested_food in fast_food != 'mcdonalds':
    print("absolutley not")

length = 12
for length in house:
    if length in house !=12:
        print('house aint ours')
print(house)    

print("# =============================================================================")
print("# tuples, for loops, lists")
print("# =============================================================================")
casa = ['cochera', 'carro', 'techo', 'puerta']
for cosas in casa:
    if cosas == 'carro':
        print('echale llave a la puerta')
    else:
        print('duermase')              
dimensions = (15,5,12,6)
for width in dimensions:
    if width == 5:
        print('width')
    elif width == 15:
        print('length')
    else:
        print('this is not our home')

toppings = ['pepperoni', 'sausage', 'x3 cheese']
requested = 'shroom'
if requested in toppings:
    print("I got you!")
elif requested not in toppings:
    print("Sorry man :{ next time")
else:
    print("is that even a topping?")
        
print("# =============================================================================")
print("# BOOLEAN")
print("# =============================================================================")

car = 'porche'
print("is car == 'audi', i think so")
print(car =='audi')

food = 'noodles'
print('the food is ummm..... what is ir??? pastaa?')
print(food=='ghetti')
print('well actually its the same')
        
print("# =============================================================================")
print("# IF ELIF")
print("# =============================================================================")

age = 11 
if age == 45:
    print('you are hitting menopause')
elif age < 18:
    print('you are a baby')
elif age >=21 or age >=1000000:
    print('ur old enough, but are you old enough to buy alcohol?, Uh lets see here --- yeah!')
else:
    print('ur a baby teen, useless')


        
print("# ====================================================")
print("# IF ELIF with DF")
print("# ====================================================")
df = pd.DataFrame(np.random.randn(10, 5), columns = ['A','B', 'C', 'D', 'E'])
print(df)

listA = df['A']
print(listA)
for num in listA:
    if num <0:
        print(df['A'].loc[(df['A'] < 0)])
    else:
        print('no more negatives')



dinner_food = ['meat', 'steak', 'keto', 'carbs']

if 'meat' in dinner_food:
    print('is this keto?')
if 'keto' in dinner_food:
    print('im a keto beast')
if 'carbs' in dinner_food:
    print('dont give that to me, im keto')
else:
    print('no fooood!')

#create a variable called alienc_color ad assign it a value of green yelllow or red

alien_color = ['green', 'yellow', 'red', 'blue']
for color in alien_color:
    if color =='green':
        print('You just earned 5 points!')
    elif color == 'yellow':
        print('You just earned 10 points!')
    elif color == 'red':
        print('You just earned 15 points!')
    else:
        print("You failed ")
#favorite fruits
favorite_fruits = ['tomato', 'grapes','kiwis','pineapple', 'avocado']
if 'tomato' in favorite_fruits:
    print('diana hates tomatoes')
if 'mango' in favorite_fruits: 
    print('mango is a fruit you guys coincide with')
if 'mango' not in favorite_fruits:
    print('mango is not a fruit you coincide with')
elif 'kiwi' in favorite_fruits:
    print ('ethan likes kiwis but diana does not')
else:
    print('thats it lol')
what_bout_this = []
if what_bout_this:
    for items in what_bout_this:
        print('nothing here')
else:
    print('its empty bro')

print("# ============================================================================================")
print("#Dictionaries")
print("# ============================================================================================")

alien_o = {'color': 'green', 'points': 5}
#adding another dict in dictionary get it?
alien_o['position_x'] = 25
alien_o['position_y'] = 30
alien_o['speed'] = 'slow'
alien_o['color'] = 'yellow'


if alien_o['color'] =='yellow':
    x_increment = 1
if alien_o['color'] =='green':
     x_increment = 4   
if alien_o['color'] =='red':
    x_increment = 15
else:
    x_increment = 35
    
alien_o['position_x'] = alien_o['position_x'] + x_increment
#interesting he for loop prints the if sttemtn if the number is surrounded by quotes
# variable = input("how old are you? ")
# if variable.strip() == '23':
#     print('gtfafm')
#     #the loop prints the else statement if we use it as a number - 23 instead of a string
# else: 
#     print('nothing')

print("# ============================================================================================")
print("#A P I s")
print("# ============================================================================================")
#Keep it secret
spotify_token='BQC1c62zkTmpXYj0d2f-FxZwm6kj_mw2bg1BXMrjQiXxk8QIEoZax1LQ4GN9HIpznxpLOA9Cs6RtnWeY91gnygwk8x2UWD-zLB0ytlJ2u737wPIsXqk3TMCStrivpESLJKKWPsOLk7kVAnZsFgCAI0QJXh8h-JMN0n0eBre0qeK174aP'
twilio_temp = +16413296395
twilio_auth = '45764a08f0da0309d12bff2022ff70b8'
twilio_act_id ='ACf52489953e06d0b615756bcfa6f4ca50'

#conda update anaconda
#conda install spyder=5.2.2


print("# ========================================================================")
print("#Using Multiple Lists")
print("# ========================================================================")

pizzas_availible = ['pepperoni', 'sausage', 'cheese']
pizzasIlike = ['pepperoni']
for toppings in pizzasIlike:
    if pizzasIlike in pizzas_availible:
        print('Adding ingredient: {pizzasIlike}')
    else:
        print()
pizzas[1]= 'marguerita'

"""

print("# ============================================================================================")
print("#Dictionaries and Web Scrapping")
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

#STEPS to FOLLOW Web Scraping
#0. If not done so, (if chrome) enable: chrome://flags/#allow-insecure-localhost as the local host server on computer

#1. load webpage with requests

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

#2. print content

soup = bs(r.content, 'lxml')

#3. convert to bs object

print(soup)
print(soup.prettify())

#HTML version of the webpage
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


#CSS version of the webpage
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
    
    
    
#Getting HTML Properties
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


#Code Navigation
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
print("#Beautiful Soup - Task")
print("# ========================================================================")

#1 Load the webpage
keith = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
#2 make bs into an object 
src = keith.content
#3 make soup an object/class
soup = bs(src, "lxml")


#task 1 - grab all the social links from the webpage
# <h2>
#  Social Media
# </h2>
# I encourage you to check out my content on all social media platforms
# <br/>
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
#   <b>
#    TikTok:
#   </b>
#   <a href="https://www.tiktok.com/@keithgalli">
#    https://www.tiktok.com/@keithgalli
#   </a>
#  </li>
# </ul>
# <h2>
    
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


#grabbing all the fin facts that have the word "is"

funfact = soup.select("ul.fun-facts li")
facts_with_is = [fact.find(string=re.compile("is")) for fact in funfact]
#gets rid of the none
#facts_with_is = [fact for fact in facts_with_is if fact]
facts_with_is = [fact.find_parent().get_text() for fact in facts_with_is if fact]


#task4 downloading an image

# Load the webpage content
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url+"webpage.html")

# Convert to a beautiful soup object
webpage = bs(r.content)

images = webpage.select("div.row div.column img")
image_url = images[0]['src']
full_url = url + image_url

img_data = requests.get(full_url).content
with open('lake_como.jpg', 'wb') as handler:
    handler.write(img_data)
"""

#ethan = 'welkl this is a story all about how my life got flip flopped upside down..\
#i would like to take a moment to just sit right there and tell you BOUT BELLAIRE'
print("# ============================================================================================")
print("#Classes and the Functions")
print("# ============================================================================================")  

  
def display_message():
    print("I am learning about functions")
    
display_message()

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}, her name is {pet_name}")

describe_pet('dog', 'noma')

def hello_name(username):
    print(f"Hello {username.title()}! Its very nice to meet you!")

hello_name("noma")

def make_shirt(size, text):
    print(f"Summary Report of Shirt: Size = {size.upper()} & Text: {text.title()}")
make_shirt('m', 'i love soda')


def make_shirt(size="M", text='I love soda'):
    print(f"Summary Report of Shirt: Size = {size.upper()} & Text: {text.title()}")
make_shirt()

#Return Values 
def full_name(first_name, last_name):
    print(f"{first_name.title()}")
    print(f"{last_name.title()}")
    
    fullname= f"{first_name} {last_name}"
    return(fullname)

musiciansFullName = full_name('jimmi', 'hendrix')
print(musiciansFullName)


def real_madrid(club_name, fc):
    print(f"{club_name.title()}")
    print(f"{fc.upper()}")
    
    full_club_name = f"{club_name.title()} {fc.upper()}"
    return (full_club_name)

realMadrid = real_madrid("real madrid", "fc")
print(realMadrid)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def rollover(self):
        print(f"{self.name} rolled over!")

noma = Dog("noma", 2)
Dog.sit(noma)

noma = {"Name": "Noma",
        "Age_(months)": 22 ,
        "Eyes": "Blue and Brown",
        "Spayed": "Yes",
        "Type_of_food": "Dry",
        "Type_of_coat": "Tan",
        "Owner_name": 'Diana Valladares',
        "Favorite_toy": "Bone" ,
        "Distractions": "Squirrels",
        "Best_friend": "Sandwich"
 }




# =============================================================================
# SELECT first_name, last_name, city, email\n",
#     "FROM customer, city\n",
#     "WHERE city_id=312\n",
# 
# =============================================================================



# WE INTERRUPT TO BRING A BRIEF MESSAGE:
import sqlite3
from sqlite3 import Error

def create_connection():
    """create a databa connection with a database that resides in the memory"""
    conn=None;
    try:
        conn =sqlite3.connect('memory:')
        print(sqlite3.version)
    except Error as e:
            print(e)
    finally: 
        if conn:
            conn.close