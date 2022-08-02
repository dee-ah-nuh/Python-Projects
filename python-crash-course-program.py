from datetime import MAXYEAR



#first program
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