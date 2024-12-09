'''
Encapsulation
--------------
This is a security mechanism (i.e when one implement we need a data and this data needs security)

Types of Attributes in Security Mechanism
------------------------------------------
1. Public Attributes
2. Protected Attributes
3. Private Attributes
'''
'''
    1. Public Attributes
    ---------------------
By default every attributes is public and can be accessed from either INSIDE or OUTSIDE of the class.
E.g name = "Kalyani"
    name is storing a data 'Kalyani'
One is accessing the variable 'Kalyani' from the class 'name' by using object reference variable or class name from outside of the class
'''
'''
    2. Protected Attributes
    ------------------------
This are protected attributes and they can be accessed WITHIN the class and in the child class only by the help of using underscore
E.g _name = "Kalyani"
This is only conventional because there's no protected attributes
'''
'''
    3. Private Attributes
    ----------------------
This attributes works only WITHIN the class we can access and this attributes begings with double underscores
E.g _ _name = "Kalyani"
'''

class Test:
    x = 10 # public attribute
    _y = 20 # protected attribute
    __z = 30 # private attribute

    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)

# testing inside of a class
t = Test()  # creating object of the class
t.m1()
'''
Output is 
10
20
30
'''

# testing outside of a class
Test.x() 
# because the other attributes are protected and private they weren't part of the suggested option after the dot . since it's outside of the class

print(Test.x)
print(Test._y)
print(Test.__z)
'''
Output is
10
20
Traceback (most recent call last):
  File "/Users/olakoya/Desktop/automationwithpython/Day30/Encapsulation.py", line 54, in <module>
    print(Test.__z)
          ^^^^^^^^
AttributeError: type object 'Test' has no attribute '__z'

There's an attribute error in the output due to the protection on the z '__z' attribute
'''
print(t._y)
'''
Output is 
20
'''
# One can access the private attribute by using onject reference with a name mangling
print(Test._Test__z) # name mangling
print(t._Test__z) # object reference variable
'''
Output is 
30
30
'''