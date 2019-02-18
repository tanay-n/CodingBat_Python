# -*- coding: utf-8 -*-


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

'''
array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''

def array123(nums):
   
    try:
        length = len(nums)
        #print (length)
        
        if length == 0:
          return False
        
        for n in range (0, length):
            o = n + 1
            p = o + 1
            p1 = nums[n]
            p2 = nums[o]
            p3 = nums[p]
            
            if p1 == 1 and p2 == 2 and p3 == 3:
                return True
            else:
                n + 1
    except:
      return False


