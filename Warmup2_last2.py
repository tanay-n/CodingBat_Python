

# Given a string, 
# return the count of the number of times that a substring length 2 appears in the string 
# and also as the last 2 chars of the string, 
# so "hixxxhi" yields 1 (we won't count the end substring).

'''
last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''

def last2(str):
    
    counter = 0
    length = len(str)
    end_string = str[-2:]
    
    if length <= 2:
        return 0
    
    for m in range (0, length):
    
        n = m + 2
        string = str[m:n]
        
        #if m == str[-2] and n == str[-1]:
            #return counter + 1 
        
        if string == end_string:
            counter = counter + 1
        m + 1
    
    print(length, m, n)
    
    p1 = length - 1
    p2 = length + 1
    if m == p1 and n == p2: 
        return counter - 1
    
    if counter > 1:
        return counter - 1
       
    return counter