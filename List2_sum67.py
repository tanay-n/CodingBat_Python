# -*- coding: utf-8 -*-

#Return the sum of the numbers in the array,
#except ignore sections of numbers starting with a 6 and extending to the next 7
#(every 6 will be followed by at least one 7). 
#Return 0 for no numbers.


'''
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
'''



def sum67(nums):
    try:
        
        length = len(nums)
        summ = 0
        n = 0
        if nums[n] == 6:
            n = n + 1
            if nums[n] == 7:
                n = n + 1
            elif nums[n] != 7:
                summ = summ
                if n == length:
                    return summ
              
              
        while nums[n] != 6:
              if n == length:
                  break
              summ = summ + nums[n]
              n = n + 1
              if n == length:
                  break
              elif nums[n] == 6:
                  while nums[n] != 7:
                      summ = summ
                      n = n + 1
                      if n == length:
                          break
                      elif nums[n] == 7:
                          summ = summ - 7
                          continue
        return summ
    
    except:
        return 0

    