# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:02:59 2017

@author: SteveJSmith1

name of pregram: MorseTranslator.py


This program will encode from morse code to
text and decode from text to morse code.

Usage1: welcome() runs the user interface

    option for encoding or decoding
    option for string or file
    
Usage2: import MorseTranslator
    
    Encoding a passed string to Morse code
        encodeText(text_string)
        
    Encoding a passed file to Morse code
        encodeFile(filepath)
        or
        encodeFile() to specify filepath in-function
        
    Decoding a passed Morse string to text
        decodeMorse(Morse_string)
        
    Decoding a passed file to Text
        decodeFile(filepath)
        or
        decodeFile() to specify filepath in-function

"""


    
#======================================

# v1

import time

def welcome():
    """
    Displays the user interface for the program
    """
    
    # collects first input
    input1 = choice1()
    
    
    if input1 == 'e':
        # encoding choice selected
        enChoice()
        
    elif input1 == 'd':
        # decoding choice selected
        deChoice()
        
    else:
        # catch quit call
        print("Quitting, goodbye!")
    return
        
def header():
    return print('-'*51)
    
    
def choice1():
    """
    This function fetches the first option;
    whether to encode to Morse or decode from Morse
    
    Do not call directly
    """
    header()
    print("Welcome to the Morse code Encoder/Decoder")
    header()
    time.sleep(0.2)
    print("Do you wish to [e]ncode or [d]ecode")
    print("Press any other key to quit")
    input1 = str(input("> "))
    header()
    return input1
    
    
def enChoice():
    """
    This function provides the options when
    [e]ncoding is selected in input1
    
    Do not call directly    
    """
    print("Encoding chosen")
    header()
    print("Do you wish to encode a typed [s]tring or a [f]ile?")
    time.sleep(0.2)
    
    # second input collected 
    input2 = str(input("> "))
    
    if input2 == 's':
        print("Please type a text string:")
        time.sleep(0.2)
        text_string = str(input("> "))
        print("Encoding to morse: ")
        # call the main encoding function to encode 
        # the text string
        return print(encodeText(text_string))
        
    elif input2 == 'f':
        # call the main function to encodeFile
        return encodeFile()
    
    else:
        print("Error: only s or f allowed as inputs")
    return
    
    
def deChoice():
    """
    This function provides the options when [d]ecode
    is set in option 1
    
    Do not call directly
    """
    print("Decoding chosen")
    header()
    print("Do you wish to decode a typed [s]tring or a [f]ile?")
    time.sleep(0.2)
    input2 = str(input("> "))
    
    if input2 == 's':
        print("Please type a string of Morse code")
        print("In the form: ")
        print("-.-. ... / -... -.-- / -... . -. . -.. .. -.-. - ")
        time.sleep(0.2)
        morse_string = str(input("> "))
        print("Decoding to text")
        return print(decodeMorse(morse_string))
    elif input2 == 'f':
        return decodeFile()
    else:
        print("Error: only s or f allowed as inputs")
    return
    
#===========================================
# File operations
#===========================================

def fileOpen(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()
        
        
def fileSave(string):
    print("Please enter a filename to save as:")
    file_name = str(input("> ")) + '.txt'
    with open(file_name, 'w', encoding='utf-8', errors='ignore') as file:
            file.write(string)
    return print("File %s" % file_name + " has been created")


#===========================================
# Text processing functions
#===========================================
        
def processTxt(text_string):
    """
    This is the module that processes the passed
    text string
    """
    import re
    # strip punctuation
    rem_punc = re.sub(r'[^\w\s]','',text_string)
    # split into words
    text_words = rem_punc.split()
    # convert to lower case and make each word a list of letters
    text_letters = [list(word.lower()) for word in text_words]
    
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    
    processed = []
    for i in range(len(text_letters)):
        words = []
        for c in text_letters[i]:
            if c in numbers:
                # call numberWords() to chage digits 
                # to words
                words.append(numberWords(int(c), p=True))
                # a list of lists is created which 
                # needs to be flattened
                words = [item for sublist in words for item in sublist]
            else:
                words.append(c)
        processed.append(words)
    return processed

    
def numberWords(key, p=False):
    """
    This function returns the word version of a 
    passed number
    
    p = True provides the processing necessary for
    conversion to morse
    """
    number_words = {1: 'One', 2: 'Two', 3: 'Three', 
                    4: 'Four', 5: 'Five', 6: 'Six',
                    7: 'Seven', 8: 'Eight', 9: 'Nine',
                    0: 'zero'}
    if p == False:
        return number_words[key]
    else:
        # returns lowercase letter required to decode
        nw = number_words[key]
        processed = [c.lower() for c in nw]
    
    return processed


#=================================================

# Main Ecoding/Decoding Functions

#=================================================

def encodeText(text_string):
    """
    Use this function to encode a text string
    to morse
    
    usage:
        text = "The 1, %cheese, I wanted"
        encodeText(text)
    """
    processed = processTxt(text_string)
    return morseEncode(processed)
    
    
def encodeFile(filepath=None):
    """
    Use this function to encode a file to Morse
    
    usage: encodeFile() or encodeFile(filepath)
    """
    if filepath is None:
        print("Please enter a full filepath to the file")
        filepath = str(input("> "))
    string = fileOpen(filepath)
    print("Processing file, please wait..")
    morse_string = encodeText(string)
    return fileSave(morse_string)
    
    
def decodeMorse(morse_string):
    """
    Use this function to decode a file from Morse
    
    Usage: decodeMorse(morse_string)
    """
    return morseDecode(morse_string)
    
    
def decodeFile(filepath=None):
    """
    Use this function to decode a file from Morse
    
    usage: decodeFile() or decodeFile(filepath)
    """
    if filepath is None:
        print("Please enter a full filepath to the file")
        filepath = str(input("> "))
    morse_string = fileOpen(filepath)
    header()
    print("Processing file, please wait..")
    text_string = morseDecode(morse_string)
    return fileSave(text_string)
        
#==================================================

# Called encoding functions

#==================================================

def morseEncode(list_of_lists):
    """
    # a list of lists is needed, this is created
    # via processTxt(text string)
    # function shouldn't be called directly
    """
    
    morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    translate = []
    for i in range(len(list_of_lists)):
        words = []
        
        for l in list_of_lists[i]:
            try:
                # attempt to look up letter
                idx = alphabet.index(l)
                # fetches morse code for letter
                words.append(morse_alphabet[idx])
            except:
            
                continue
        translate.append(' '.join(words))
    return ' / '.join(translate)
    
    
def morseDecode(morse_string):
    """
    Assumes file contains a single string of the form
    '.-' '-...' / 
    where whitespace is a letter seperator and /
    is a word seperator
    
    should not be called directly
    """
    
    morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    morse_words = morse_string.split(' / ')
    morse_letters = [w.split(' ') for w in morse_words]
    
    translate = []
    for i in range(len(morse_letters)):
        words = []
        for ml in morse_letters[i]:
            try:
                idx = morse_alphabet.index(ml)
                words.append(alphabet[idx])
            except:
                continue
        translate.append(''.join(words))
    return ' '.join(translate)

#=============================================


    
     
if __name__ == '__main__': 
    welcome()

  