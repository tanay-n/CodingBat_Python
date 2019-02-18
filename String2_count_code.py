# -*- coding: utf-8 -*-


#Return the number of times that the string "code" appears anywhere in the given string, 
#except we'll accept any letter for the 'd', so "cope" and "cooe" count.


'''
count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''

def count_code(str):
    length = len(str)
    
    count = 0
    
    for p in range(0, length - 3):
        q = p + 1
        r = q + 1
        s = r + 1
        
        if str[p] == "c" and str[q] == "o" and str[s] == "e":
            count = count + 1
        p + 1
        
    return count



