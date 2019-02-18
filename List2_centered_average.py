# -*- coding: utf-8 -*-


#Return the "centered" average of an array of ints, 
#which we'll say is the mean average of the values, 
#except ignoring the largest and smallest values in the array. 
#If there are multiple copies of the smallest value, ignore just one copy, 
#and likewise for the largest value. Use int division to produce the final average. 
#You may assume that the array is length 3 or more.

'''
centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
'''

def centered_average(nums):
    ma = max(nums)
    mi = min(nums)
    unique = len(set(nums))
    
    if unique == 1:
        return nums[0]
    
    elif unique != 1:
        for number in nums:
            if number == ma:
                nums.remove(number)
        for number in nums:
            if number == mi:
                nums.remove(number)        
        length = len(nums)
        avg = sum(nums)/length
        return int(avg)


# trial

numb = [1, 2, 3, 4, 5, 6, 6]
numb2 = [7, 7, 7]
ma = max(numb)


for number in numb:
    if number == ma:
        numb.remove(number)

print(numb)
print(len(set(numb)), len(set(numb2)))
    

