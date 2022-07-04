# -*- coding: utf-8 -*-
"""

Cesar Gutierrez
CPSC 223P-01
March 8th
cesarg7@csu.fullerton.edu

"""

def computersWeapon():
    
    from random import randint
    number =  randint(1,3)
    return number

def results(roundcounter, playerWins, computerWins, ties):

    print("Computer: " + str(computerWins))
    print("You: " + str(playerWins))
    print("Ties: " + str(ties))

    if playerWins > computerWins:
        print("You won!")

    elif playerWins < computerWins:
        print("Computer Won!")
    
    else:
        print("You tied!")

    #print("Total Rounds Played: " + str(roundcounter))


print("You have choosen to play Rock, Paper, or Scissors")
print("You can choose between R for Rock, P for Paper, S for Scissors, or Q to quit")

keepLooping = True
roundcounter = 0
playerWins = 0
computerWins = 0
ties = 0

while(keepLooping):
    print("")
    answer = input("Make your choice: R, P, S, or Q ---> ")
    computersHand = computersWeapon()

    if computersHand == 1 and answer == "R" or answer == 'r':

        roundcounter +=1
        ties += 1
        print("Computer chose Rock. Call it a draw.")
    
    elif computersHand == 2 and answer == "R" or answer == 'r':

        roundcounter +=1
        computerWins +=1
        print("Computer chose Paper. Computer wins!")

    elif computersHand == 3 and answer == "R" or answer == 'r':

        roundcounter +=1
        playerWins +=1
        print("Computer chose Scissors. You win!")

    elif computersHand == 1 and answer == "P" or answer == 'p':

        roundcounter +=1
        playerWins +=1
        print("Computer chose Rock. You win!")

    elif computersHand == 2 and answer == "P" or answer == 'p':

        roundcounter +=1
        ties += 1
        print("Computer chose Paper. Call it a draw.")

    elif computersHand == 3 and answer == "P" or answer == 'p':

        roundcounter +=1
        computerWins +=1
        print("Computer chose Scissors. Computer wins!")

    elif computersHand == 1 and answer == "S" or answer == 's':

        roundcounter +=1
        computerWins +=1
        print("Computer chose Rock. Computer wins!")
    
    elif computersHand == 2 and answer == "S" or answer == 's':

        roundcounter +=1
        playerWins +=1
        print("Computer chose Paper. You win!")
    
    elif computersHand == 3 and answer == "S" or answer == 's':

        roundcounter +=1
        ties += 1
        print("Computer chose Scissors. Call it a draw.")
    
    elif answer == "Q" or answer == 'q':

        print("")
        print("Not everyone can handle a game like this. Terminating Program...")
        results(roundcounter, playerWins, computerWins, ties)
        keepLooping = False

    else:
        print("Invalid Entry. Try Again")