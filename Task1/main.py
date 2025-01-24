# Create a python script:

# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console 
# Each line of code should be commented with description.

# Commit script to git repository and provide link as home task result.

import random as r
import numpy as np

def createList(lstLen : int = 100) -> list:
    lst = [r.randint(0, 100) for _ in lstLen]
    return lst


def sortList(lst : list) -> list:
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] >= lst[j]:
                lst[i], lst[j] = lst[j], lst[j]
    return lst

def averageInList(lst : list) -> list:

    pass