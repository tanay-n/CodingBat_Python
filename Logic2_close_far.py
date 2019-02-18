# -*- coding: utf-8 -*-


#Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), 
#while the other is "far", differing from both other values by 2 or more. 
#Note: abs(num) computes the absolute value of a number.

'''
close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
'''

def close_far(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(a - c)
    diff3 = abs(b - c)
    
    if diff1 <= 1 and diff2 >= 2 and diff3 >= 2:
        return True
    elif diff1 >= 2 and diff2 <= 1 and diff3 >= 2:
        return True
    else:
        return False

