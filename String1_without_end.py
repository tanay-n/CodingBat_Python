# -*- coding: utf-8 -*-


#Given a string, return a version without the first and last char, so "Hello" yields "ell". 
#The string length will be at least 2.

'''
without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
'''

def without_end(str):
    end = len(str) - 1
    return str[1:end]
