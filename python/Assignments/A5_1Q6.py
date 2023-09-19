# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:07:17 2023

@author: q
"""

#-------------------------------------------------try to make ur own ------------------------------

# Write a menu driven program to practice Set functions.
# Write a program to accept names from users and store it in a set.
# Display the following menu:
# print("""1. delete element if exists otherwise
# do not show any errr""")
# print("2. add a elemet")
# print("3. create one more set")
# print("4. union of 2 sets")
# print("4. intersection of 2 sets")
# print("5. difference of 2 sets")
# print("6. convert set into frozenset")
# print("6. exit")


'''
# This part Remaining 
print("6. convert set into frozenset")

'''

from A5_1Q6_module import *

while True: 
    case = int(input("""
                    1. delete element
                    2. add a elemet
                    3. create one more set
                    4. union of 2 sets
                    5. intersection of 2 sets
                    6. difference of 2 sets
                    7. convert set into frozenset
                    8. Print set
                    9. Exit
                    Enter Choice:"""))



    if case == 1:
        x = input("""Enter from which set you want to delete element : 
        1. Set a
        2. Set b
        choice [a/b]: """)
        if x == 'a':
            delset('a')
        elif x == 'b':
            delset('b')
        
    if case == 2:
        addele()

    if case == 3:
        createset()

    if case == 4:
        union()

    if case == 5:
        intersect()

    if case == 6:
        difference()

    if case == 7:
        frozenset()

    if case == 8:
        x = input("""Enter which set you want to print : 
        1. Set a
        2. Set b
        3. Set a and b 
        choice [a / b / ab]: """)
        if x == 'a':
            print(a)
        elif x == 'b':
            print(b)
        elif x == 'ab':
            print(a,b)

    if case == 9:
        print("Exiting......")
        break
