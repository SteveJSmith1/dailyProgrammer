# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:11:22 2017

@author: SteveJSmith1

Creates a password of a given length, at random
containing lowercase letters, capitalised letters
and numbers

usage:
    createPassword()
    for a default length of 8
    createPassword(10)
    for a 10 character long password
"""


import random

def welcome():
    print("-"*33)
    print("       Password Generator       ")
    print("-"*33)
    print("Enter required length of password")
    
    try:
        l = int(input("> "))
    except:
        raise ValueError("Must give a number")
    
    
    return print(createPassword(l))
     
def lowLet(k=1):
    return random.sample("abcdefghijklmnopqrstuvwxyz", k)
    
def capLet(k=1):
    return random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k)

def num(k=1):
    return random.sample("0123456789",k)
    

def createPassword(length=8):
    """
Creates a password of a given length, at random
containing lowercase letters, capitalised letters
and numbers

usage:
    createPassword()
    for a default length of 8
    createPassword(10)
    for a 10 character long password
    """
    
    
    
    password = []
    for i in range(length):
        # choose lower, capitalised or a number
        # at random
        choice = random.choice([1,2,3])
        if choice == 1:
            password.append(lowLet())
        if choice == 2:
            password.append(capLet())
        if choice == 3:
            password.append(num())
    # a list of lists is the result so flatten into 
    # a list and then join
    return ''.join([item for sublist in password for item in sublist])


if __name__ == '__main__':
    welcome()
    
    