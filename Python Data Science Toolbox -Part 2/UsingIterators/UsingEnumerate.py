# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:02:52 2018

@author: Hitesh
enumerate() returns an enumerate object that produces a sequence of tuples, 
and each of the tuples is an index-value pair.

In this exercise, you are given a list of strings mutants and 
you will practice using enumerate() on it by printing out a list of tuples and unpacking the tuples using a for loop.

INSTRUCTIONS
100 XP
Create a list of tuples from mutants and assign the result to mutant_list.
 Make sure you generate the tuples using enumerate() and turn the result from it into a list using list().
Complete the first for loop by unpacking the tuples generated by calling enumerate() on mutants.
 Use index1 for the index and value1 for the value when unpacking the tuple.
Complete the second for loop similarly as with the first, 
but this time change the starting index to start from 1 by passing it in as an argument to the start parameter
 of enumerate(). Use index2 for the index and value2 for the value when unpacking the tuple.
"""
# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pride']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1,value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2,value2 in enumerate(mutants,start=1):
    print(index2, value2)


"""
output:
[(0, 'charles xavier'), (1, 'bobby drake'), (2, 'kurt wagner'), (3, 'max eisenhardt'), (4, 'kitty pride')]
0 charles xavier
1 bobby drake
2 kurt wagner
3 max eisenhardt
4 kitty pride
1 charles xavier
2 bobby drake
3 kurt wagner
4 max eisenhardt
5 kitty pride

"""
