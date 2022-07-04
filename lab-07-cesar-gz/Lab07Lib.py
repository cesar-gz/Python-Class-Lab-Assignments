# -*- coding: utf-8 -*-
"""
Cesar Gutierrez
CPSC 223P-01
Thu Feb 23rd, 2022
cesarg7@csu.fullerton.edu
"""

# Constant definition
import abc
from typing import Counter


ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

# Function definitions below this line

def is_alpha(string):
    "has one parameter (a string). It returns True if all of the characters in the string are upper case or lower case ASCII letters (it returns False otherwise)."
    
    digitList = list(DECIMAL_DIGITS)
    for x in string:
        if x in digitList:
            return False
    return True

def is_digit(string):
    "has one parameter (a string). It returns True if all of the characters in the string are ASCII decimal digits (it returns False otherwise)."
    
    abcList = list(ASCII_LOWERCASE+ASCII_UPPERCASE)
    for x in string:
        if x in abcList:
            return False
    return True

def to_lower(string) -> str:
    "has one parameter (a string). It returns the string which is a copy of the parameter, but where all of the upper case ASCII letters have been converted to lower case ASCII letters. Any digits or lower case letters will be left alone"
    
    copy = ""
    capsList = list(ASCII_UPPERCASE)
    counter = -1
    length = len(string)
    
    for x in string:
        counter += 1
        if counter >= length:
            break
        elif x not in capsList:
            copy = copy + x
        else:
            y = ord(x)
            z = y + 32
            copy = copy + chr(z)
    return copy

def to_upper(string):
    "has one parameter (a string). It returns the string which is a copy of the parameter, but where all of the lower case ASCII letters have been converted to upper case ASCII letters. Any digits or upper case letters will be left alone."
    
    copy = ""
    abcList = list(ASCII_LOWERCASE)
    counter = -1
    length = len(string)
    
    for x in string:
        counter += 1
        if counter >= length:
            break
        elif x not in abcList:
            copy = copy + x
        else:
            y = ord(x)
            z = y - 32
            copy = copy + chr(z)
    return copy

def find_chr(string1, string2):
    "has two parameters (both strings), where the second parameter must be of length 1. It returns the lowest index where the second parameter is found within the first parameter (it returns -1 if the second parameter is not of length 1 or is not found within the first parameter)"

    counter = -1
    index = 0
    length = len(string2)
    if length != 1:
        return -1
    elif string2 not in string1:
        return -1
    else:
        for x in string1:
            counter += 1
            if string2 in x:
                index = counter
                break
    return index

def find_str(string1, string2):
    "has two parameters (both strings). It returns the lowest index where the second parameter is found within the first parameter (it returns -1 if the second parameter is not found within the first parameter)"
    
    if string2 not in string1:
        return -1
    
    index = 0 
    end = 0

    while index < len(string1):

        if string1[index+end] != string2[end]:
            index += 1
            end = 0
            continue
        end += 1
        if end == len(string2):
            return index
    
    return -1

def replace_chr(string1, string2, string3):
    "has three parameters (all strings), where the second and third parameters must be of length 1. It returns the string which is a copy of the first parameter, but where all occurrences of the second parameter have been replaced by the third parameter (it returns the empty string if the second or third parameter are not of length 1). If there are no occurrences of the second parameter in the first, it returns a copy of the first parameter."

    copy = ""

    length = len(string2)
    if length != 1:
        return copy
    length = len(string3)
    if length != 1:
        return copy
    
    test1 = find_chr(string1, string2)
    if test1 == -1:
        copy = string1
        return copy
    
    count = -1

    for x in string1:
        count += 1
        if string2 in x:
            copy = copy + string3
        elif string2 not in x:
            copy = copy + string1[count]
        elif count >= len(string1):
            break

    return copy    

def replace_str(string1, string2, string3):
    "has three parameters (all strings). It returns the string which is a copy of the first parameter, but where all occurrences of the second parameter have been replaced by the third parameter. If there are no occurrences of the second parameter in the first, it returns a copy of the first parameter. If the second parameter is the empty string, it returns a copy of the first parameter."

    copy = ""

    test1 = find_str(string1, string2)
    if test1 == -1:
        copy = string1
        return copy

    if string2 == "":
        copy = string1
        return copy
    
    strLength = len(string1)
    subLength = len(string2)
    count = -1

    if strLength >= subLength:
        for x in range(strLength):
            count += 1
            if string1[x:x+subLength] == string2:
                copy = copy + string3
                copy = copy + string1[x+subLength:strLength]
                break
            elif string1[x:x+subLength] != string2:
                copy = copy + string1[x]
            elif count >= len(string1):
                break

    return copy

stringTest = "The quick brown fox"
stringTest2 = "quick"
stringTest3 = "fast"
c = replace_str(stringTest, stringTest2, stringTest3)
print(c)
