from datetime import MAXYEAR

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
print(f"what do you say eh?")

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
variable = input("how old are you? ")
if variable.strip() == '23':
    print('gtfafm')
    #the loop prints the else statement if we use it as a number - 23 instead of a string
else: 
    print('nothing')

 
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










 


















































#ethan = 'welkl this is a story all about how my life got flip flopped upside down..\
#     i would like to take a moment to just sit right there and tell you BOUT BELLAIRE'
     



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