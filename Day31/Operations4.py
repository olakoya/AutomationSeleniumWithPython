# Approach 1 is from ==> import Module name
# ------------------------------------------

import Calculator2
import ArithmetricOperations4
import Calculator2, ArithmetricOperations4

Calculator2.add(10,40)
Calculator2.mul(23,34)
ArithmetricOperations4.mul(56,12)
ArithmetricOperations4.add(99,10)

'''
Output is
50
782
672
109

With the help of the different modules we are importing respected functions
And this approached is best suited for this scenario
'''

# Approach 2 is from ==> from modulename import functions and classes
# -------------------------------------------------------------------

from Calculator2 import add, mul

# add(12,14)
# mul(2,12)

'''
Output is
26
24
'''

from ArithmetricOperations4 import add, mul

add(28,34)
mul(12,12)

add(12,14)
mul(2,12)

'''
Output is
62
144
26
24
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

from ArithmetricOperations4 import *

mul(9,99)
add(30,30)

'''
Output is
5643
1588
891
60
'''