# -*- coding: utf-8 -*-
"""

Cesar Gutierrez
CPSC 223P-01
Mon Feb 14, 2022
cesarg7@csu.fullerton.edu

"""

import lists

sports_teams = [lists.football_teams, lists.baseball_teams, lists.basketball_teams]

# Print out all the school lunches on the menu, but substitute bratwurst 
# wherever you see hot dogs
# Use list comprehension. Just print the list directly so the output will
# include the brackets and quotations (['item 1', item 2' ... and so on])
newList = [x if x!= 'hot dogs' else 'bratwurst' for x in lists.school_lunches]
print(newList)

# Use zip to iterate over two lists at the same time
# Print out questions and answers in a loop
# Format them: "What is your <question>? My <question> is <answer>."
ziplist = []
for questions, answers in zip(lists.questions, lists.answers):
    print("What is your {0}? My {0} is {1}".format(questions, answers))
    ziplist.append((questions, answers))

# Manipulate the nested lists of sports teams to print all teams from New York
# and all teams from Los Angeles.  Just print the lists directly so the output will
# include the brackets and quotations (['team 1', team 2' ... and so on])

#professor said to make an outer for loop that sifts through sports team's lists, like list1 then list 2 list3
# then an inner loop that sifts through that list and finds substring "new"

#y = 0
#nyList = [y for y in x if "New York" in y]

mainList = []

for x in sports_teams:
    nyList = [y for y in x if "New York" in y]
    mainList = mainList + nyList
print(mainList)
    
mainListTwo = []

for x in sports_teams:
    laList = [y for y in x if "Los " in y]
    mainListTwo = mainListTwo + laList
print(mainListTwo)