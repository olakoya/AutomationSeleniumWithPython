'''
Dealing with module inside package?

Modules and Packages - 2
-------------------------
Sys module in python is required and enables interaction of our python program with system

Absolute Path: /Users/olakoya/Desktop/automationwithpython/Day32/Pack1
Both / and ' are path separators
\ (back slash) is use as an escape characters in python
To avoid issues when using windows operating system, one need to use the escape escape \\ character
r strings can be used at the beginning of the path location

Location of package will help in interaction between 2 packages/modules
E.g
'''

import  sys
sys.path.append("/Users/olakoya/Desktop/automationwithpython/Day32/Pack1") # path file has all the variables path and through it one needs to specify were the package us located
sys.path.append(r"/Users/olakoya/Desktop/automationwithpython/Day32/Pack2")
# one needs to right-click on pack1 to get the path location
# parent directory for this is Day 32
# Pack1 consisting of Module_1 and Pack2 consisting of Module_2

# Approach 1
# import Module_1
# import Module_2
#
# Module_1.display()
# Module_2.show()

'''
Output is 
This is display function from module1
This is show function from module2
'''
# Approach 2
# from Module_1 import display
# from Module_2 import show
#
# display()
# show()

'''
Output is
This is display function from module1
This is show function from module2
'''

# Approach 3
from Module_1 import *
from Module_2 import *

display()
show()

'''
Output is
This is display function from module1
This is show function from module2
'''

# import sys # the sys is used to communicate between the programme and the system by specifying the location
# sys.path.append(r"/Users/olakoya/Desktop/automationwithpython/Day31") # specifying the location where the module is located either in directory or package
#
# import a
#
# obja = a.Animal()
# obja.display()

'''
Output is 
I like Cow
'''

'''
To be able to import inside the client module one needs to specify 2 locations
'''

'''
Using Approach 3 above to execute after adding new path in Line 20 and commenting in line 23

Output is 
This is display function from module1
This is show function from module2
This is display function from module1
This is show function from module2
'''
# 2 different packages and 2 different modules in lines 19 and 20 after moving Pack2 file from Pack1 into the Day32 file

'''
Afterwards another execution is conducted and output is
This is display function from module1
This is show function from module2
This is display function from module1
This is show function from module2

Above are the ways in which one import modules which are inside in packages inside directory
'''

'''
Type of Approaches used above are:
----------------------------------
1. Import modulename
2. From module import functions, classes
3. From module import *

As seen in Day2 keywords file
'''