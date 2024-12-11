# Approach 1 is from ==> import Module name
# ------------------------------------------

import a,b

# with the help of an object one can call the method and variable in the class a and b

obja = a.Animal()
obja.display()

objb = b.Bird()
objb.display()

'''
Output is
I like Cow
I like Parrot

Approach one is more suitable and recommended
'''

# Approach 2 is from ==> from modulename import functions and classes
# -------------------------------------------------------------------

from a import Animal
from b import Bird

Animal().display()
Bird().display()

'''
Output is
I like Cow
I like Parrot
'''


# Approach 3 is from ==> from modulename import * (* means all)
# -------------------------------------------------------------

from a import *
from b import *

Animal().display()
Bird().display()

'''
Output is
I like Cow
I like Parrot
'''