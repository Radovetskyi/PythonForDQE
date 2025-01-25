# Create a python script:

# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console 
# Each line of code should be commented with description.

# Commit script to git repository and provide link as home task result.

import random as r

def createList(lstLen : int = 100) -> list:
    # Using list comp to create list with default len 100 and with random numbers in it
    lst = [r.randint(0, 100) for _ in range(lstLen)] 
    return lst


def sortList(lst : list) -> list:
    """
    Here we must compare number with n index to n+1 index. 
    If it's `n` greater then `n+1` -> we swapping them and repeat till end of list
    """
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] >= lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def averageInList(lst : list) -> list:
    oddList = [] # List for odds
    evenList = [] # List for evens
    for num in lst: # Iterate through list
        if num % 2 == 0: # Check if number is even
            evenList.append(num) # If it's true -> append it to proper
        else:
            oddList.append(num) # If false -> append to another one
    return sum(oddList) / len(oddList), sum(evenList) / len(evenList) # rerurning averages

lst = createList() # Initialing list
print('New list is: ', lst, '\n')

sortedlst = sortList(lst,) # Sorting list
print('Sorted list: ', sortedlst, '\n')

oddAverage, evenAvarage = averageInList(sortedlst)
print('Average for odd numbers in sortedlst is :', oddAverage, '\n',
      'Average for even numbers in sortedlst is :', evenAvarage, '\n')