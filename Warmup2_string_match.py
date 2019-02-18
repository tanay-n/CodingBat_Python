# -*- coding: utf-8 -*-

#Given 2 strings, a and b, 
#return the number of the positions where they contain the same length 2 substring. 
#So "xxcaazz" and "xxbaaz" yields 3, 
#since the "xx", "aa", and "az" substrings appear in the same place in both strings.

'''
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''

def string_match(a, b):
    
        len_a = len(a)
        len_b = len(b)
        
        if len_a < len_b:
            frange = len_a
        else:
            frange = len_b
        
        #n = 0
        #o = n + 1
        
        #while o <= frange:
        
            counter = 0
            for n in range(0, frange - 1):
                
                o = n + 1
                
                a1 = a[n]
                a2 = a[o]
                b1 = b[n]
                b2 = b[o]
    
                if a1 == b1 and a2 == b2:
                    counter = counter + 1
                
                n + 1
            
        return counter
    
        
        
            
