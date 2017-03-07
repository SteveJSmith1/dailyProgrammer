# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 13:46:52 2017

@author: SteveJSmith1

create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
    
your name is (blank), you are (blank) years old, and your username is (blank)

for extra credit, have the program log this information in a file to be accessed later.


C1E.py
"""

def infoSave():
    import csv
    import time
    time.sleep(1)
    name = str(input("Please enter your name: "))
    time.sleep(1)
    age = int(input("Please enter your age: "))
    time.sleep(1)
    username = str(input("Please enter your reddit username: "))
    
    fields = [name, age, username]
    with open('Reddit_Usernames.csv', 'a', newline='') as csvfile:
        infowriter = csv.writer(csvfile)
        infowriter.writerow(fields)
    return print("""
    Your name is %s, you are %d years old
    and your username is %s
    """ % (fields[0], fields[1], fields[2]))
    


infoSave()
