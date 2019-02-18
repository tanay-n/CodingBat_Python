
#Given a non-empty string like "Code" return a string like "CCoCodCode".

'''
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def string_splosion(str):
    
    word = len(str)+1
    add = ""
    
    for letter in range(0, word):
        
        new_word = str[:letter]
        letter+1

        add = add + new_word
    
    return add
    