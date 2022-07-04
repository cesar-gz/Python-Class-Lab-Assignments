
# -*- coding: utf-8 -*-
"""
Cesar Gutierrez
CPSC 223P-01
Thu Apr 6, 2022
cesarg7@csu.fullerton.edu
"""

from audioop import mul
import random

# Hangman class.
class Hangman:
    
    def __init__(self, word, triesAllowed):
        self.myWord = word
        self.myWordnoEdits = word
        self.tries = triesAllowed
        self.lettersUsed = ""
        self.usersGuess = ""
        self.hangManWord = "-" * len(self.myWord)
        self.hangManWordcopy = "-" * len(self.myWord)

    def Guess(self, letter):
        """Pass in a letter (length = 1) and check to see if it is in the word.
            If it is, replace blanks in display word with letter and return True
            If not, decrement the number of tries left and return False
        """
        self.usersGuess = letter        

        if self.usersGuess in self.myWordnoEdits:

            print("Good Guess! Letters used: " + self.lettersUsed)
            
            if self.usersGuess in self.lettersUsed:
                return

            self.lettersUsed += self.usersGuess + "-"
            multipleLetters = self.myWord.count(self.usersGuess)
            #print(self.myWord)

            if multipleLetters == 1:
                    
                index = self.myWord.index(self.usersGuess)
                self.hangManWord = self.hangManWord[:index] + self.usersGuess + self.hangManWord[index+1:]
                self.myWord = self.myWord.replace(self.myWord[index], "-", 1)

            elif multipleLetters > 1:
                    
                multipleLetters += 1    
                while(multipleLetters > 1):
                    index = self.myWord.index(self.usersGuess)
                    self.hangManWord = self.hangManWord[:index] + self.usersGuess + self.hangManWord[index+1:]
                    self.myWord = self.myWord.replace(self.myWord[index], "-", 1)
                    multipleLetters -= 1
                
            elif self.myWord == self.hangManWordcopy:
                self.tries = 0
            
            return True

        else:
            self.tries -= 1
            self.lettersUsed += self.usersGuess + "-"
            print("Too bad! Letters used: " + self.lettersUsed)
            return False

    def GetNumTriesLeft(self):
        """Return the number of tries left""" 
        return self.tries
    
    def GetDisplayWord(self):
        """Return the display word (with dashes where letters have not been guessed)
        i.e. the word happy with only the letter 'p' guessed so far would be '--pp-'"""
        return self.hangManWord
            
    def GetLettersUsed(self):
        """Return a string with the list of letters that have been used"""
        return self.lettersUsed

    def GetGameResult(self):
        """Return True if all letters have been guessed. False otherwise"""
        if self.hangManWord == self.myWordnoEdits:
            return True
        else:
            return False

    def DrawGallows(self):
        """Optional: Return string representing state of gallows"""
        pass

# implement the logic of your game below
if __name__=="__main__":
    # Read all the words from the hangman_words.txt file
    wordFile = open("Class Lab Assignments\lab-08-cesar-gz\hangman_words.txt", "r")
    wordFileText = wordFile.read()
    wordFile.close()
    
    # Seed the random number generator with current system time
    random.seed()
    
    # Convert the string of words in wordFile to a list,
    wordList = wordFileText.split()

    # then get a random word using
    min = 1
    max = 210000
    randomIndex = random.randint(min, max)
    randomWord = wordList[randomIndex]
    wordLength = len(randomWord)

    # Instantiate a game using the Hangman class
    Game = Hangman(randomWord, wordLength)
    
    # Use a while loop to play the game
    while(Game.GetNumTriesLeft() > 0):

        word = Game.GetDisplayWord()
        print("Here's your word so far: " + word)
        tries = Game.GetNumTriesLeft()
        print("You have " + str(tries) + " guesses left")
        print("")

        userInput = input("Guess a letter: ") 
        
        Game.Guess(userInput)
        print("")

        if Game.GetNumTriesLeft() == 0:
            successfulGame = Game.GetGameResult() 
            if successfulGame == True:
                print("Congratulations!  You won!! The word was " + randomWord)
            elif successfulGame == False:
                print("You lost.  The word was " + randomWord)