# -*- coding: utf-8 -*-
"""
Cesar Gutierrez
CPSC 223P-01
2/2/2022
cesarg7@csu.fullerton.edu
"""

import sys

# This is my second Python program. It inspects strings.

x = sys.argv[0]
words = x.split()
shortest = "cats"
longest = "dog"

for i in words:
    if len(i) < len(shortest):
        shortest = i
    if len(i) > len(longest):
        longest = i

print("Shortest word:", shortest)
if len(shortest) == 1:
    print("It is", len(shortest), "character")
if len(shortest) > 1:
    print("It is", len(shortest), "characters")

print("Longest word:", longest)
if len(longest) == 1:
    print("It is", len(longest), "character")
if len(longest) > 1:
    print("It is", len(longest), "characters")