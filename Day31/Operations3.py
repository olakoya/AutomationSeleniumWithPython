# creating another module but by calling the operators from the Calculator module
# To make available the functions we need to follow the approaches declared in Modules and Packages file

# Approach 1 is from ==> import Module name (this is a key to import from one module to another)
# ----------------------------------------------------------------------------------------------

import Calculator2 # importing only the module

Calculator2.add(50, 30)
Calculator2.mul(89, 55)

'''
Output is 
80
4895
'''

# Approach 2 is from ==> from modulename import functions and classes
# -------------------------------------------------------------------

from Calculator2 import add, mul

add(989, 576)
mul(674, 823)

'''
Output is 
1565
554702
'''

# Approach 3 is from ==> from modulename import * (* means all)
# -------------------------------------------------------------

from Calculator2 import *

mul(57, 99)
add(767, 821)

'''
Output is
5643
1588
'''
