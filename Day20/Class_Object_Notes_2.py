'''
Constructor
------------
Is special type of method and used for specail purposes
And the special purpose is that it is used to create and initialise instance variables
Once one creates an object constructor is automatically invoked

To design a variable inside a class we need to create and initialise instance variables i.e.
To design a variable inside a class we need a constructor (_ _init_ _)
(_ _init_ _) is the unique name of the constructor
To define a constructor we need to specify a unique (_ _init_ _) name
Once we create an object Test() and reference t1 i.e. 
different houses from previous file (Day 19 CO1) where constructed with the help of a blueprint (i.e. class)
To create an instant variable we need object construction to store a data which is automatically executed
Per object constructor is executed once
Self is mandatory parameter
Construction is also optional

class Test: # class creation
    a = 10 # class variables
    def test(self): # function created in a class is called method i.e creating a method
        print(self.a) # this is accessing the class variable # "self" is helping to access and mandatory parameter

t1 = Test() # object

From the above codes;
Class is a logical entity and t1 = Test() object (referred to as house) is a physical entity
Object (t1 = Test()) is an instance of a class
With the reference to t1 = Test() variable, one can have access to the members of the class and it's method
What comprises of a class is 1. variable, 2. method, 3. object reference variable
t1 reference is a variable because it's pointing to the Test () object
Test () object represent each house are an independent object
With the reference of object reference t1 one can access the members of the class i.e method (a=10) and print(t1.a) and t1 test()
One couldn't access is previously without the construction because it's a special type of method and used for specail purposes
Once we create an object t1 = Test() by default and construction is located inside the class by the default it will be executed
Each object t1 is independent of each other i.e. t1.....t8

'''