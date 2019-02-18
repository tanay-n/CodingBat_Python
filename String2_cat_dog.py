# -*- coding: utf-8 -*-


#Return True if the string "cat" and "dog" appear the same number of times in the given string.

'''
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
'''

def cat_dog(str):
    length = len(str)
    
    catcount = 0
    dogcount = 0
    
    for c in range(0, length - 2):
        d = c + 1
        e = d + 1
        
        if str[c] == "c" and str[d] == "a" and str[e] == "t":
            catcount = catcount + 1
        
        if str[c] == "d" and str[d] == "o" and str[e] == "g":
            dogcount = dogcount + 1
        
        c + 1
        
    if catcount == dogcount:
        return True
    else:
        return False