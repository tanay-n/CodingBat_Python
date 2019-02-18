# -*- coding: utf-8 -*-

#Given an array of ints, 
#return True if the array is length 1 or more, and the first element and the last element are equal.

'''
same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
'''

def same_first_last(nums):
    
    length = len(nums)
    first = nums[0]
    last = nums[-1]
    
    if length >= 1 and first == last:
        return True
    elif length == 1:
        return True
    else:
        return False
