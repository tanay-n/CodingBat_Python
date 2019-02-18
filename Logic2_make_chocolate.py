# -*- coding: utf-8 -*-


#We want make a package of goal kilos of chocolate. 
#We have small bars (1 kilo each) and big bars (5 kilos each). 
#Return the number of small bars to use, assuming we always use big bars before small bars. 
#Return -1 if it can't be done.

'''
make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''


def make_chocolate(small, big, goal):
    bigk = big * 5
    summ = small + bigk
    diff1 = goal - bigk
    
    d = divmod(goal, 5)
    
    if summ < goal:
      return -1
    elif bigk <= goal and small >= diff1:
      return diff1
    elif small > (goal - (d[0]*5)):
      return goal - (d[0]*5)
    elif small < d[1]:
      return -1
    elif small == (goal - (d[0]*5)):
      return small




