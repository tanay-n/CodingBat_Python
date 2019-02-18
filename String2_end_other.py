# -*- coding: utf-8 -*-

#Given two strings, return True if either of the strings appears at the very end of the other string, 
#ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
#Note: s.lower() returns the lowercase version of a string.


'''
end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
'''


def end_other(a, b):
      a_low = a.lower()
      b_low = b.lower()
      
      alen = len(a_low)
      blen = len(b_low)
      
      
      if alen == blen and a_low == b_low:
          return True
      elif blen > alen and a_low == b_low[-alen:blen]:
          return True
      elif alen > blen and b_low == a_low[-blen:alen]:
          return True
      else:
          return False
        