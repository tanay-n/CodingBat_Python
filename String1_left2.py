# -*- coding: utf-8 -*-

#Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. 
#The string length will be at least 2.

'''
left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
'''

def left2(str):
    
    first2 = str[:2]
    the_rest = str[2:]
    
    if len(str) > 2:
        return the_rest + first2
    else:
        return str
    
      


