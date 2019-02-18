# -*- coding: utf-8 -*-


#Given 2 strings, a and b, 
#return a string of the form short+long+short, 
#with the shorter string on the outside and the longer string on the inside. 
#The strings will not be the same length, but they may be empty (length 0).

'''
combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
'''

def combo_string(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        long = a
        short = b
    else:
        long = b
        short = a
        
    return short + long + short
