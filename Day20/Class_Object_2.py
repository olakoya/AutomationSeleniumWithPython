# Checkout Day 19 Class_Object_Notes for Method Notes

class Test: # class name i.e class or blueprint
    def __init__(self): # declaration of constructor name and contains (self) mandatory parameter
        print("Construction Execution") # when "def __init__(self):" is executed it will print construction statement
    def m1(self): # simple method and (self) is a simple mandatory parameter and test name is m1
        print("Method Execution") # print statement
t1 = Test() # a contsructor is name calling a particular class and this attempt is called an object. One can have many
t2 = Test() # t1 is a reference variable
t3 = Test() # object
'''
Output from the above 3 objects executed
Construction Execution
Construction Execution
Construction Execution

Method Codes Line 2 and 3 automatically invoke because it's contstruction

And to call the method in line 4 and 5, what we need to do is add this object codes below;
'''
t1.m1() # m1 - method name must be the same in all the objects
t2.m1()
t3.m1()
t1.m1()
'''
Output from the above 3 objects executed
Method Execution
Method Execution
Method Execution
Method Execution
'''
'''
                        Method                           |                           Construction
-------------------------------------------------------------------------------------------------------------------------
1. Name of method can be any name                        |  1. Constructor name should be always __init__
2. Method will be executed if we call that method        |  2. Constructor will be executed automatically at the time of object creation.
3. Per object, method can be called any number           |  3. Per object, Construction will be executed only once
4. Inside method we can write business logic             |  4. Inside Constructor we have to declare and initialize instance variable

'''