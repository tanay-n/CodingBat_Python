# -*- coding: utf-8 -*-


# Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
# The array length may be less than 4.

'''
array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''

#def array_front9(nums):
    length = len(nums)
    #print(length)
    counter = 0
    n = 0
    for n in range(0, length):
        if n < 4:
            if nums[n] == 9:
                counter = counter + 1
                n + 1
            else:
                n + 1
        else: 
            return counter
    return counter


def array_front9(nums):
    #length = len(nums)
    n = 0
    try:
        for n in range(0, 4):
            if nums[n] == 9:
                return True
            else:
                n + 1
        return False
    except:
        return False