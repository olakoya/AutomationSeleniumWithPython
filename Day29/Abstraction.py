'''
Abstraction
------------
For a project I'm implementing Login or Sign in Function for logging into application after getting clarity on requirements
    i. We decalre a method in a class for the physical functionality (this is implemnting the interface)

For Abstract we have 2 important things to Abstract
1. Abstract Method
2. Abstract Class
'''
#---------------------------------------------------
'''
1. Abstract Method
-------------------
Sometimes when we have no idea about implementation but still can declare a method

Abstract methods has only declaration but no implementation
Child classes are responsible for creating/providing an implementation for parent class abstract methods
To declare abstract method one needs to use a decorator, that is @abstractmethod decorator
From ABC Module we can call Abstract Method decorator (@abcmodule ====> @abstractmethod)

2. Abstract Class
------------------
This is partially implemented class called an Abstract Class
And this can contain both Abstract and Non-Abstract Methods in respect to abstract method and abstract class
To declare an abstract class one needs to use abc (Abstract Base Class) module, that is @abcmethod module

Every abstract class must be inherited from the ABC Class (@abstractmethod ===> @abcmodule)

@abc module needs to import from @abstractmethod decorator

Set of statements are called ==> Functions
Functions saved to a file is called ==> Module
Group of modules is called ==> Package
ABC is a Py file 
And Py file is a Module

E.g
'''
# creating a class and inside it we are creating a method with a parameter
# importing a class from ABC module
from abc import ABC, abstractmethod # ABC and abstractclass are from abc module

class Fruit(ABC): # this is abstract class, and specifying parent class as 'ABC' and base class for all classes
    @abstractmethod # before any method one needs to declares an abstract method
    def taste(self): # fruit class contining abstract methon in lines 35 and 36
        pass # non-abstract method

'''
4 Types of Scenarios in Abstract
------------------------------------
1. Without Inherit Without Abstract Method
2. With Inherit Without Abstract Method
3. With Inherit With Abstract Method
4. Without Inherit With Abstract Method
'''
#--------------------------------------------------
'''
1. Without Inherit Without Abstract Method
-------------------------------------------
The class Test below is not inherited from the ABC class and doesn't have any method it's an unimplented and impartial class
'''
# class Test:
#     pass
# t = Test () # creating an object of the respected class
'''
Output is blank and no error
'''
#-------------------------------------------------------
'''
2. With Inherit Without Abstract Method
-----------------------------------------
The below class is imported from the ABC module and inherited from the ABC class
'''
from abc import ABC

# class Test(ABC):
#     pass
# t = Test () # creating an object of the respected class
'''
Output is blank and no error
'''
#-------------------------------------------------------
'''
3. With Inherit With Abstract Method
--------------------------------------
This class is inherited, implemented and also contain an abstract method
'''
# from abc import ABC

# class Test(ABC): # abstract class containing an abstract method
#     @abstractmethod
#     def m1(self): # defining a method
#         pass
# t = Test () # creating an object of the respected class
# above is a TypeError
'''
Output is 
File "/Users/olakoya/Desktop/automationwithpython/Day29/Abstraction.py", line 95, in <module>
    t = Test () # creating an object of the respected class
        ^^^^^^^
TypeError: Can't instantiate abstract class Test without an implementation for abstract method 'm1'
'''
#-----------------------------------------------------------
'''
4. Without Inherit With Abstract Method
-----------------------------------------
This class wihtout inherit and doesn't contain anything
E.g
'''
# from abc import abstractmethod

# class Test: # abstract class containing an abstract method
#     @abstractmethod
#     def m1(self): # defining a method
#         pass
# t = Test () # creating an object of the respected class
# t.m1()
'''
Output is blank
'''
'''
Conclusion
------------
- If a class contains at least one abstract method and if we are extending ABC class then instantiation is not possible.
- It it's Abstract class with abstract method instantiation is not possible.
- Parent class abstract methods should be implemented in child classes.
- Otherwise we cannot instantiate child class.
- If we are not creating child class object then we won't get any error.
- If one is extending abstract class and doesn't override it's abstract method
- Then child class instantiate is impossible
E.g
'''
from abc import ABC, abstractmethod

class Vehicle: # abstract class containing an abstract method
    @abstractmethod
    def noofwheels(self): # defining a method
        pass
class Bus(Vehicle):
    pass

b = Bus()
b.noofwheels()
# v = Vehicle()
# v.noofwheels()
'''
Output is
raceback (most recent call last):
  File "/Users/olakoya/Desktop/automationwithpython/Day29/Abstraction.py", line 140, in <module>
    v.noofwheels()
TypeError: Vehicle.noofwheels() missing 1 required positional argument: 'self'

Output after add child method in lines 140 to 144
blank
'''