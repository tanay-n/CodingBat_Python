# -*- coding: utf-8 -*-


# Given an array of ints, return the number of 9's in the array.

'''
array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''

def array_count9(nums):
    # nums = []
    elements = len(nums)
    counter = 0
    print("elements: ", elements)
    for element in nums:
        if element == 9:
            counter = counter + 1
            element + 1
            print("loop: ", counter)
        else:
            element + 1
    return counter


name = [1, 2, 3, 4, 5, 6, 7, 8, 9]
name_count = len(name)
print(name_count)

n = 1
element = name[n]
print(element)