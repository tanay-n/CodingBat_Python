# -*- coding: utf-8 -*-


#Return the number of times that the string "hi" appears anywhere in the given string.


'''
count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
'''


def count_hi(str):
    
    length = len(str)
    print(length)
    counter = 0
    for f in range(0, length - 1):
        s = f + 1
        if str[f] == "h" and str[s] == "i":
            counter = counter + 1
        f + 1
      
    return counter

count_hi('abc hi ho')




