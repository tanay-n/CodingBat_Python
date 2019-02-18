# -*- coding: utf-8 -*-


#Given 2 arrays of ints, a and b, 
#return True if they have the same first element or they have the same last element.
#Both arrays will be length 1 or more.

'''
common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
'''

def common_end(a, b):
    
    afirst = a[0]
    alast = a[-1]
    bfirst = b[0]
    blast = b[-1]

    al = len(a)
    bl = len(b)
    
    if afirst == bfirst or alast == blast:
        return True
    else:
        return False
    
    