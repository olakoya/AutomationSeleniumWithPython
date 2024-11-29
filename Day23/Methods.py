# Checkout Day 19 Class_Object_Notes for Methods Notes
'''
Types of Methods in a Class
----------------------------
1. Instance Methods
    It is the use of instance variables inside the inside method implementation
    To access instance method inside a class we use self variable 
    And if we want to access outside, we use object reference variable

2. Class Methods
    It is the use of class or static variables inside method implementation
    We use @classmethod decorator to declare the function/method
    We use cls variable as the parameter
    And to access class method we need to use classname or object reference variable

3. Static Methods
    In general these methods are general utility methods
    Inside these methods we won't use any instance or class variables.
    Here we won't provide self or cls arguements at the time of declaration
    We can declare static method explicitly by using @staticmethod decorator
    Also, we can access static method by using classname or object reference variable
    If any method is a static method then self is considered as a parameter at the time 
    of calling then we need to pass value to self as as well
'''

class Test:
    b = 20 # ==> CLASS VARIABLE

    def __init__(self,a): # ==> CONSTRUCTOR
        self.a = a # ==> INSTANCE VARIABLE

    def m1(self): # ==> INSTANCE METHOD
        print(self.a) # ==> ACCESSING SELF INSTANCE VARIABLE

    def m2(self):  # ==> INSTANCE METHOD
        self.m1()  # ==> ACCESSING M1 VIA SELF

    @classmethod 
    def m3(cls): # ==> CLASS METHOD
        print(Test.b) # ==> INSTANCE VARIABLE

    @staticmethod
    def m4(): # ==> STATIC METHOD
        print(4+5)

t = Test(10) # OBJECT
t.m1() # OBJECT REFERENCE VARIABLE
t.m2()
Test.m3()
t.m3()
t.m4()
Test.m4

'''
Output is
10
10
20
20
9
'''