# creating an addition function
def add(a,b): 
    print(a+b)

# creating a multiplication function
def mul(a,b):
    print(a*b)

# passing values to the 2 parameters
# add(10, 20)
# mul(100, 200)

'''
Output is
30
20000

calling functions from the same module
'''
# Approach 3 is from ==> from modulename import * (* means all)
# -------------------------------------------------------------

from Calculator2 import *
from ArithmetricOperations4 import *

mul(57, 99)
add(767, 821)

'''
Output is
5643
1588
'''