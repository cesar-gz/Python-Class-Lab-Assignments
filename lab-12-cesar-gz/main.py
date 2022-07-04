"""
cesar gutierrez
CPSC 223P-01
Weds Apr 27, 2022
cesarg7@csu.fullerton.edu

quiz is weds 5/11/22
next weds is on zoom
quiz is on files, exceptions, modules, web api
threads will not be on it
itll be over weeks 12, 13, 14
"""

import threading
import time

file = open("synch.txt", "w")
file.close()

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

def threadFunction(myList):
    with open("Class Lab Assignments\lab-12-cesar-gz\synch.txt", "a") as file:
        for i in range(20):
            for j in range(26):
                file.write(f"{myList[j]} ")
            file.write("\n")
            if myList == abc:
                time.sleep(1)
            



threadA = threading.Thread(target =threadFunction, args=(number,))
threadA.start()


threadB = threading.Thread(target =threadFunction, args=(abc,))
threadB.start()


threadA.join()
threadB.join()
