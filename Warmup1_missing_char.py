
# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

'''
missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
'''

def missing_char(str, n):
  try:
      string_length = len(str)-1
      n < string_length
      
      # treat string as an array
      stop = str[:n]
      start = str[n+1:]
      return (stop + start)
  
  except:
      return "Please enter a valid 'n' value from 0 to the end of the string length"   

