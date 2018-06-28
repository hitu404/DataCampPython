# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 21:05:54 2018

@author: Hitesh
you can apply a conditional statement to test the iterator variable by adding an if statement in the optional predicate expression part after the for statement in the comprehension:

[ output expression for iterator variable in iterable if predicate expression ].

You will use this recipe to write a list comprehension for this exercise. You are given a list of strings fellowship and, using a list comprehension, you will create a list that only includes the members of fellowship that have 7 characters or more.

Use member as the iterator variable in the list comprehension. For the conditional, use len() to evaluate the iterator variable. Note that you only want strings with 7 characters or more.
"""
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member)>=7]

# Print the new list
print(new_fellowship)


"""

output
['samwise', 'aragorn', 'legolas', 'boromir']



Using conditional part 2 
You will work on the same list, fellowship and, using a list comprehension and an if-else conditional statement in the output expression, create a list that keeps members of fellowship with 7 or more characters and replaces others with an empty string. Use member as the iterator variable in the list comprehension.

INSTRUCTIONS
In the output expression, keep the string as-is if the number of characters is >= 7, else replace it with an empty string - that is, '' or "".
"""

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member)>=7 else "" for member in fellowship]

# Print the new list
print(new_fellowship)
