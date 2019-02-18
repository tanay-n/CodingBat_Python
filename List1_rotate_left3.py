# -*- coding: utf-8 -*-


#Given an array of ints length 3, 
#return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


'''
rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
'''

def rotate_left3(nums):
    
    p1 = nums[0]
    p2 = nums[1]
    p3 = nums[2]

    nums2 = [p2, p3, p1]
    
    return nums2
    

