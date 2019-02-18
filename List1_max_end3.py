# -*- coding: utf-8 -*-

#Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
#and set all the other elements to be that value. Return the changed array.

'''
max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
'''

def max_end3(nums):
    
    p1 = nums[0]
    p3 = nums[2]

    if p1 > p3:
        nums2 = [p1, p1, p1]
        return nums2
    if p3 > p1:
        nums2 = [p3, p3, p3]
        return nums2
    if p1 == p3:
        nums2 = [p1, p1, p1]
        return nums2
    
    