# -*- coding: utf-8 -*-
"""

Cesar Gutierrez
CPSC 223P-01
Weds Feb 09, 2022
cesarg7@csu.fullerton.edu

"""

fruits = ["grape", "mango", "nectarine", "pineapple", "banana", 
          "apple", "orange", "pear", "strawberry", "avocado"]

vegetables = ["zucchini", "asparagus", "kale", "spinach", "broccoli",
              "celery", "beets", "bok choy", "brussels sprouts", "arugula"]

combinedList = fruits + vegetables
print("There are " + str(len(combinedList)) + " elements in the combined list")

newlySortedList = sorted(combinedList)

for item in newlySortedList:
    print(item)
    if item == "mango":
        break

reversedList = []
n = 0
m = 19

for item in newlySortedList:
    reversedList.insert(n, newlySortedList[m])
    n +=1
    m -=1
    if n == 20:
        print(reversedList)
        break
