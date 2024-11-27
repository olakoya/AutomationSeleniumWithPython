# Local Variable
# ---------------
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
