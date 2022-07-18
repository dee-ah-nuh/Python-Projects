#Here is a self updating clock function, just run it and it'll self update itself until you hit CTRL-C
import datetime
import time


def clock():
    while True:
        print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
        time.sleep(1)

clock() 
