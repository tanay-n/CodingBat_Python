# -*- coding: utf-8 -*-


#Return the sum of the numbers in the array, returning 0 for an empty array.
#Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

'''
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
'''


def sum13(nums):
  
    length = len(nums) - 2
    summ = 0
    
    if 13 not in nums:
        return sum(nums)
    
    track = 0
    for n in nums:
        if n == 13:
            track = track + 1
            
    if nums[-1] == 13 and track == 1:
        return sum(nums) - 13
    
    count = 0
    for n in range(0, length):
        if nums[count] != 13:
            summ = summ + nums[count]
            count = count + 1
            print(nums[count])
        elif nums[count] == 13:
            summ = summ
            count = count + 2
        
    return summ


sum13([1, 2, 2, 1, 13])


