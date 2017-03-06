# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 13:25:35 2017

@author: SteveJSmith1

This program implements the Ceaser Cypher on an
inputted string or file

"""

import codecs

def welcome():
    print("Welcome to the Ceaser Cypher encoder/decoder")
    print("Do you wish to [e]ncode or [d]ecode a typed string")
    print("Or encode/decode a [f]ile?")
    
    choice = str(input("> "))
    if choice == 'e':
        s = cencode()
        print(s)
        
    elif choice == 'd':
        s = cdecode()
        print(s)
        
    elif choice == 'f':
        s = fileCypher()
        
    else:
        print("Error: only e, d or f are allowed as inputs")
    return 
    
def cencode(string=None):
    """
    encodes a string with the ceaser cypher
    if none is passed, it asks for input
    """
    if string == None:
        print("Enter a string to encode:")
        string = str(input("> "))
    
    enc = codecs.getencoder("rot-13")
    return enc(string)[0]
    
def cdecode(string=None):
    """
    decodes a string with the ceaser cypher
    if none is passed, it asks for input
    """
    if string == None:
        print("Enter a string to decode:")
        string = str(input("> "))
    dec = codecs.getdecoder("rot-13")
    return dec(string)[0]
    
def fileCypher():
    """
    When a filepath is entered it decodes/encodes
    and writes to a file
    """
    print("Enter full path including file")
    filename = str(input(">"))
    with open(filename, 'r', errors='ignore') as f:
        string = f.read()
        
    
    print("%s opened" % filename)
    print("Do you wish to [e]ncode or [d]ecode the file?")
    
    choice = str(input("> "))
    if choice == 'e':
        print("Enter a filename to save it as:")
        file_name = str(input("> "))+'.txt'
        with open(file_name, 'w', errors='ignore') as file:
            file.write(cencode(string))
        print("File %s" % file_name + " has been created")
        
    elif choice == 'd':
       print("Enter a filename to save it as:")
       file_name = str(input("> "))+'.txt'
       with open(file_name, 'w', errors='ignore') as file:
            file.write(cdecode(string))
       print("File %s" % file_name + " has been created")
      
    else:
        print("Error: only e or d are allowed as inputs")
    
    
    return 
    
if __name__ == '__main__':
    
    welcome()
    




    