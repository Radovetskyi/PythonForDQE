# Write a code, which will: 
 
# 1. create a list of random number of dicts (from 2 to 10) 
 
# dict's random numbers of keys should be letter, 
# dict's values should be a number (0-100), 
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}] 

# 2. get previously generated list of dicts and create one common dict: 
 
# if dicts have same key, we will take max value, and rename key with dict number with max value 
# if key is only in one dict - take it as is, 
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42} 
# Each line of code should be commented with description. 

# Commit script to git repository and provide link as home task result.

import random as r
import string

def createListOfDicts(n : int) -> list:
    num_dicts = r.randint(2, 10) # create variable for a list of random number of dicts (from 2 to 10)
    
    letters = list(string.ascii_lowercase) # Letters for keys

    dict_list =[] 

    for i in range(num_dicts):
        # random n of keys
        n_keys = r.randint(3, n)
        # unique keys from all letters
        c_keys = r.sample(letters, n_keys)
        # creating dicts
        d = {k: r.randint(0, 100) for k in c_keys}
        dict_list.append(d)
    return dict_list

def mergeDicts(d : list) -> dict:
    data = {}
    # iterate through all dicts
    for i, dicts in enumerate(d):
        # checking key value pairs
        for key, value in dicts.items():
            # if key was not repeated we add it to dict
            if key not in data:
                data[key] = {
                    'value': value,
                    'index': i,
                    'count': 1 
                }
            # if it was reapeted we enhance count
            else:
                data[key]['count'] += 1
                # checking if new value greater then we already have and write index of new bigger value and it's value
                if value >= data[key]['value']:
                    data[key]['value'] = value
                    data[key]['index'] = i
    # result dict                
    result = {}
    for key, i in data.items():
        # write original name of key
        if i['count'] == 1:
            result[key] = i['value']
        else:
            # if key repeated several times
            dict_index = i['index'] + 1
            new_key = f'{key}_{dict_index}'
            result[new_key] = i['value']

    return result

d = createListOfDicts(10)
print(d)

d = mergeDicts(d)
print(d)