#!/usr/bin/env python2.7
# Author: Sneha GUNDA

"""
Usage: The Usage of this code is simple. You can either call the 
file from cmd line or can import the file as module. 

Ex: 
1) Call from cmdline :
$ python matching_brackets.py

returns: 
  output in a outfile 'brackets-matched.txt' in working directory
  
2) import the file as module in python prompt:

>>> from matching_brackets import *
>>> isMatched("()[]{}")
()[]{}
>>> isMatched("([{}])")
([{}])
>>> isMatched("([{)]}")
-1
>>>

If isMatched returns the string if it is balanced and returns -1 if not balanced.
Returned strings are stored in the 'brackets-matched.txt' file
"""

import sys, re

##create an output file to store the balanced strings
out_file = open('brackets-matched.txt','wb')

 
""" this function reads each atring from the input file and 
checks if it is balanced with the brackets or not
    """
def isMatched(characters):
    # declaring the class objects
    stack = []
    ok = True
    openers = {
    '(': ')',
    '{': '}',
    '[': ']',
     }
    closers = set(openers.values())
    '''Check for delimiters balanced, if not return -1 '''
    for i, c in enumerate(characters, start=1):
        if c in openers:
            stack.append(openers[c])
        elif c in closers:
            if not stack or c != stack.pop():
                return i

    '''return i if there are characters in stack, else -1 '''
    if stack: return i
    else: return -1
   
'''This function parses thru the 
    input file lines, calls function isMatched and 
    writes the final list to output file'''
def scan_file(file):
        with open(file, 'r') as f:
            for line in f:
                try:
                    characters = line
                except Error: continue
                position = isMatched(characters)
                if position == -1: out_file.write(line)

if __name__ == '__main__':

    ''' Read from the input file '''
    scan_file('brackets.txt')
    out_file.close()
