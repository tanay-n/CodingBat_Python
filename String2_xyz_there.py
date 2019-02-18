# -*- coding: utf-8 -*-


#Return True if the given string contains an appearance of "xyz" 
#where the xyz is not directly preceeded by a period (.). 
#So "xxyz" counts but "x.xyz" does not.

'''
xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''

def xyz_there(str):
    try:
      
        if str == "xyz":
          return True
          
        if str[0] == "x" and str[1] == "y" and str[2] == "z":
          return True
          
        length = len(str)
        if length > 3:
            for n in range(0, length):
                o = n + 1
                p = o + 1
                q = p + 1
                
                if str[n] != "." and str[o] == "x"  and str[p] == "y" and str[q] == "z":
                    return True
                else:
                    n + 1
        else:
            return False
    except:
        return False


