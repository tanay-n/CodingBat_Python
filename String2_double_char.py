# -*- coding: utf-8 -*-


#Given a string, return a string where for every char in the original, there are two chars.

'''
double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
'''


def double_char(str):
    
    new_string = ""
    for letter in str:
        double = letter * 2
        new_string = new_string + double
    return new_string