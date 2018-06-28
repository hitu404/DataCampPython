# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 23:03:15 2018

@author: Hitesh
Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, write a list comprehension that produces a list of numbers consisting of the squared values of i.
"""

# Create list comprehension: squares
squares = [i*i for i in range(0,10)]
print(squares)