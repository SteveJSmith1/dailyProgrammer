# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:10:29 2017

@author: SteveJSmith1

This program implements the algorithm for
Russian Peasant Multiplication


name of program: C2E - Peasant Multiplication
"""

import time

def welcome():
    
    # Obtain inputs


    print("Welcome to the peasant multiplier")
    print("Please enter two integers to multiply")
    time.sleep(0.2)
    num1 = input("First number: ")
    num2 = input("Second number: ")
    
    # call the function intTest to test whether inputs
    # are ints
    intTest(num1, num2)
        
    return 
    
def header():
    return print("%5s %15s" % ("LHS", "RHS"))
 
def header2(num1, num2):
    return print("You are multiplying %s by %s" % (num1, num2))

def process(num1, num2, h=True):
    
    # print header if function called directly
    # suppressed for the call from processFloat
    if h == True:
        header2(num1, num2)
        
    
    time.sleep(0.1)
    # print other header
    header()
    
    # create lists for the algorithm
    l1 = []
    l2 = []
    print("%5d %15d" % (num1, num2))
    l1.append(num1)
    l2.append(num2)
    
    # implement the algorithm
    while num1 != 1:
        num1 = int(num1/2)
        num2 = int(num2*2)
        print("%5d %15d" % (num1, num2))
        
        l1.append(num1)
        l2.append(num2)
    
    # fetching the odd numbers from l1
    idx = [l1.index(i) for i in l1 if i % 2 !=0]
    # new lists creating the reuired numbers
    lhs = [l1[j] for j in idx]
    rhs = [l2[j] for j in idx]
    print("Removing even numbers on the LHS leaves:")
    header()
    
    # printing the numbers that are used
    for i in range(len(lhs)):
        print("%5d %15d" % (lhs[i], rhs[i]))
    
    print("Summing the RHS gives:")
    
    # making a nice output, suppresing newline
    for j in range(len(rhs)- 1):
        print(str(rhs[j]) + " +", end=' ')
    
    print(str(rhs[(len(rhs)-1)]) + " =", end = ' ')
    print(sum(rhs))
    return sum(rhs)
    
def processFloat(num1, num2):
    # print header
    header2(num1, num2)
    time.sleep(0.1)
    
    # extracting the decimal places from the floats
    num1_dp = int(str(num1)[::-1].find('.'))
    num2_dp = int(str(num2)[::-1].find('.'))
    # counting decimal places
    dp = num1_dp + num2_dp
    # stripping decimal paints
    dp_rem_1 = int(str(num1).replace('.',''))
    dp_rem_2 = int(str(num2).replace('.',''))
    
    print("Removing Decimal points leaves: %d % d" %(dp_rem_1, dp_rem_2))
    
    # passing the integers to process()
    dec_sum = process(dp_rem_1, dp_rem_2, h=False)
    # converting the result to a string
    str_sum = str(dec_sum)
    # putting the decimal point back in
    dec_answer = float(str_sum[:-dp]+'.'+str_sum[-dp:])
    # using the number of decimal places as 
    # output precesion
    print("Putting the decimal point back: {:.{prec}f}".format(dec_answer, prec=dp))
   
    return 
    
def intTest(num1, num2):
    # testing inputs for types and converting
    # to correct type
    if '.' in str(num1) and '.' in str(num2):
        # floats are passed to processFloat()
        processFloat(float(num1), float(num2))
    elif '.' in str(num1) and '.' not in str(num2):
        
        changed = float(str(num2) + '.0')
        
        processFloat(float(num1), changed)
        
    elif '.' in str(num2) and '.' not in str(num1):
        changed = float(str(num1) + '.0')
        processFloat(changed, float(num2))
    
    else:
        # ints passed to process()
        process(int(num1), int(num2))
        
 



    
if __name__ == '__main__':
    welcome()
    





