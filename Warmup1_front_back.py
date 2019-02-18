# -*- coding: utf-8 -*-

# Given a string, return a new string where the first and last chars have been exchanged.

'''
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''

def front_back(str):
    try:
        first = str[0]
        n = len(str)
        last = str[-1]
        
        if n == 1:
            return str
        else:
            return last + str[1:n-1] + first
    except:
        str = ""
        return ""


