# -*- coding: utf-8 -*-
"""

Cesar Gutierrez
CPSC 223P-01
Wed March 02, 2022
cesarg7@csu.fullerton.edu

"""

import string

# This is the function that you must write the code for
def numWordsSpoken(candidate, word):
    """This function returns the number of times a given word was 
    spoken by a given speaker"""

    if candidate in "OBAMA":
        return obamaDict[word]
    elif candidate in "ROMNEY":
        return romneyDict[word]
    else:
        return 0


# This code will extract the data from the debate file and read it into one big
# string named debateString
debateFile = open("Class Lab Assignments\lab-05-cesar-gz\debate.txt", "r")
debateString = debateFile.read() 
debateFile.close()

# This code will extract the data from the stop words file and read it into one big
# string named stopWordsString
stopWordsFile = open("Class Lab Assignments\lab-05-cesar-gz\stopWords.txt", "r")
stopWordsString = stopWordsFile.read()
stopWordsFile.close()

# empty dictionaries
obamaDict = {} 
romneyDict = {}
lehrerDict = {}

# empty lists
obamaLists = []
romneyLists = []

# initialize bools to false
obamaFound = {"PRESIDENT", "BARACK", "OBAMA:"}
romneyFound = {"MR.", "ROMNEY:"}
lehrerFound = {"MR.", "JIM", "LEHRER:"}
personSpeaking = ""

# function to add passed words to obamaDict dict{}
def obamaDictAdd(w):
    # if the word was already found in the dictionary,
    # increase its count by 1
    if w in obamaDict:
        obamaDict[w] += 1
    # if the word wasnt found, set its count to 1
    else:
        obamaDict[w] = 1

def romneyDictAdd(w):
    if w in romneyDict:
        romneyDict[w] += 1
    else:
        romneyDict[w] = 1

def lehrerDictAdd(w):
    
    if w in lehrerDict:
           lehrerDict[w] += 1
    else:
       lehrerDict[w] = 1

# parsing thru the text while flagging who is speaking
# and calling their respective dictAdd functions to add
# to their proper dictionaries
for w in debateString.split():

    # obama was found to be speaking, so personSpeaking
    # is set to obama
    if w in obamaFound:
        personSpeaking =  "obama"
        # keep parsing after we set obama to be speaking
        continue

    elif w in romneyFound:
        personSpeaking = "romney"
        continue
 
    elif w in lehrerFound:
        personSpeaking = "lehrer"
        continue

    # convert to lowercase for more parsing
    w = w.lower()
    
    # remove punctuation
    w = w.strip(string.punctuation)

    # remove remaining punctuation that hasnt been removed
    w = w.replace('-', "")
    w = w.replace("'", "")

    # disregard any words that are in the stopWordsString
    if w in stopWordsString:
        continue

    # depending on who is speaking, their respective dictAdd 
    # is called to add to their proper dictionaries
    if personSpeaking == "obama":
        obamaDictAdd(w)
    if personSpeaking == "romney":
        romneyDictAdd(w)
    if personSpeaking == "lehrer":
        lehrerDictAdd(w)

# append the dictionary items to each list in value, key order
# for printing and sorting purposes
for key, val in obamaDict.items():
    obamaLists.append((val, key))
for key, val in romneyDict.items():
    romneyLists.append((val, key))

#sort and reverse the lists for printing purposes
obamaLists.sort(reverse=True)
romneyLists.sort(reverse=True)

#print obamas top 40 most used words
print("\nObama")
for i in range(40):
    print(f"{obamaLists[i][0]}:{obamaLists[i][1]}", end=" ")

print("\n\nRomney")
for i in range(40):
    print(f"{romneyLists[i][0]}:{romneyLists[i][1]}", end=" ")