# -*- coding: utf-8 -*-


#Given 2 strings, return their concatenation, except omit the first char of each. 
#The strings will be at least length 1.

'''
non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
non_start('ab', 'x') → 'b'
'''

def non_start(a, b):
  
  la = len(a)
  lb = len(b)
  
  if la == 1 and lb == 1:
    return ""
  if la == 1 and lb > 1:
    return b[1:lb]
  if la > 1 and lb == 1:
    return a[1:la]
  if la > 1 and lb > 1:
    return a[1:la] + b[1:lb]
  
  
        
    
        
        
