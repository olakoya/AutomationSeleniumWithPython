# Checkout Day 21 Class_Object_Notes_3 for Local Variable Notes

# Example 1 Local Variable
# --------------------------
class Test:
    a = 10 # class variable
    def __init__(self):
        self.b = 20 # instance variable
        c = 30 # local variable 
        # => no using of class name for declaring c, no using of "self" from constructor during creator of vairiable c is called LOCAL VARIABLE
        print(c)

        # defining another method
        def m1(self):
            print(self.c) # inside this method one can't access c
            print(Test.c)

t = Test()
t.m1()
'''
Output is 
30

Once a local variable is created it's only a property of the particular method it's created in and not a property of other method
Even though it's declared in a class, it's only applicable to the method it's located in
'''
# Example 2 Local Variable
# ---------------------------
class Test:
    b = 50 # b is a CLASS VARIABLE and it's constant, also located out of a constructor class 
    def __init__(self,a): # constructor method 
        print(a) # INSTANCE VARIABLE
        print(Test.b)
    def m1(self): # m1 method and a function
        c = 100 # LOCAL VARIABLE
        print(c)
    def m2(self): # m2 method and a function
        d = 200 # LOCAL VARIABLE
        print(d)
Test(10) 
Test(20) 
t = Test(30)
t.m1()
t.m2()
'''
Output is 
10
50
20
50
30
50
100
200
'''
# local variable is only accessed inside their specific methods
# c = 100 is local variable to m1 while d = 200 is local variable to m2
# Therefore c can't access m2 method likewise d can't access m1 method
