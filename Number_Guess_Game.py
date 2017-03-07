# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:23:24 2017

@author: SteveJSmith1

[difficult] challenge #1
submitted 5 years ago by nottoobadguy
we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program that will guess numbers between 1-100, and respond appropriately based on whether users say that the number is too high or too low. Try to make a program that can guess your number based on user input and great code!

c1d.py


Work in process
"""
import time

def guess(floor, ceiling):
    r = [floor, ceiling]
    guess = int(sum(r)/2)
    print("""
    My guess is %d""" % guess)
    time.sleep(0.2)
    choices = ['h', 'l', 'c']
    guide = str(input("""
    Is your number [h]igher, [l]ower 
    or is my guess [c]orrect?: """ ))
    if guide not in choices:
       guide = str(input("""
    Only h,l or c allowed as inputs: """ ))
    
    return guess, guide
    
def welcome():
    print("""
    Welcome to the number guessing game
    
    Please enter an integer range for me to guess from:
    """)
    time.sleep(0.2)
    
    floor = int(input("Lowest value: "))
    ceiling = int(input("Highest Value: ")) + 1
    return floor, ceiling
    
    
def start():
    
    floor, ceiling = welcome()
    
    count = 0
     
    g, guide = guess(floor, ceiling)
    while guide != 'c':
    
        if guide == 'h':
            floor = g
            g, guide = guess(floor, ceiling)
            count += 1
        elif guide == 'l':
            ceiling = g
            g, guide = guess(floor, ceiling)
            count += 1
    
    
    print("""
    Your number is %d, it took me %d guesses""" % (g, count))
        
    return
  
if __name__ == '__main__':
    start()
     
