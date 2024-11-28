'''
Class and Object
----------------

Types of Object Oriented Programming Languages Principles (OOPS)
-----------------------------------------------------------------
1. Class and object
2. Inheritance
3. Abstraction
4. Polymorphism
5. Encapsulations


Types/Structures of Programming Langugages
-------------------------------------------
1. Structured: This programe doesn't support object oriented programming principles => C, Python
2. Object Based: This supports only class and object => VB, VBScript, Python
3. Object Oriented: This supports OOPS ==> Java, C++, C#, Python

In Python, without creating a class one can write a code.
Also with class and object one can write a code in Python.
Python is fully an object oriented programming language.

'''
'''
Class
------
Class is nothing but a design of a blueprint
A blueprint is a design called a class
In Python everything is treated as an object therefore, we need to create an object
To create an object one needs a blueprint
Blueprint is a logical entity that is, it will not occupy space in the memory 
Except for physical entities, and that will only occupy some space in the memory
If you want to build a house we need a design
The design document will occupy some space
And this design document is nothing but a class which is a blueprint in logical memory
That is, it wouldn't occupy any space in the memory
You create an object and that object is your house
The house consists of bedroom, kitchen, bathroom, toilet etc and as such one will require some requirements/properties
A class contains properties and operations
With the help of a blueprint one will create an object
From object there will be a specification
And those specifications are called properties (variables) and operations of an object
These properties are also called attributes while operations can be called actions
With the help of class, one can create an object and for the object one will have some specific properties
Class consists of variables (properties) and methods (behaviour). In blueprint we specify variables and objects
Properties or Attributes of objects are called Variables
E.g
        Class Test ==> A class which is a creation/declaration of a blueprint
                a = 10 ==> inside class we have some class variables a = 10
                def m1(self): ==> for a variable we have a method with parenthese open and close def m1(self):
                    print(self.a) ==> inside the method we are accessing a particular variable which we've defined
Test() ==> Is an object or an instance of a class
t ==> is an object reference variable
class ==> blueprint
object ==> house
object reference variable ==> house address

Class consists of a variable and a method

'''
'''
Object
-------
Object is a physical existence of a class
Object will occupy any space in the memory
We create a class with a def keyword

Syntax
------
    i. We create a keyword ==> class
    ia. Class returns consists of "Documentation string" and just a comment which is optional
    ii. Followed by class name ==> class_name
    iii. Inside class we have varaibles ==> variables
    iv. And methods of an object ==> methods
How to call a function? We need a function name with an open and close parenthesis ==> class_name()
We call a class with the help of class_name and  open and close parentheses ()
If we want to specify the object we call the class name
We need a physical existence of a class to create an object.
Function is an entry point, and one calls it with the help of keyword
And calling the class is creating an object

        class class_name: # class creation
                "documentation string"
                variables
                methods
        
        class name() # class calling => object of a particular class
'''
'''
Method
-------
Method is a function created/declared inside a class

That is, Method is a property of class

We create function by using a def keyword, function name, open and close parentheses and colon 

By default method has a self parameter which is nothing but a function deeclared inside of method

If self is not declared it becomes an issue because it's property of a particular class

Self is a mandatory parameter for a method of a class that is, a class where the method is defined

Once we create a class we can create any number of objects and this objects are independent

To objects we can give reference and this is independent 

With the help of reference variable, we call variables and methods of object
'''

'''
Types of Methods
-----------------
1. Instance Method
        This is use to update or retrieve instance-specific data, like modifying a user's profile details.
2. Class Method
        This is use for for class-wide operations, like keeping track of the total number if the users in a system.
3. Static Method
        This is use for utitlity functions, like validating a username format with out needing class or instance data.
        Utilities consists of reusable functions

'''
'''
Constructor
------------
Constructor is a special type of method with unique name __init__(self is optional)
To declare and initialize instance variables
Once we create an object constructor is automatically invoked or executed
per object constructor is executed once
E.g
        Class Test ==> A class which is a creation/declaration of a blueprint
                a = 10 ==> inside class we have some class variables a = 10
                def __init__(self): ==> creating a constructor with a self parameter
                    print(self.a) ==> inside the method we are accessing a particular variable which we've defined
                def m1(self): ==> for a variable we have a method with parenthese open and close def m1(self):
                    print(self.a) ==> inside the method we are accessing a particular variable which we've defined
t = Test() ==> Is an object or an instance of a class together with "t" which is an object reference variable
Test() ==> defining another object calling it Test() will execute the constructor to 10
Test() ==> Similarly another object in the constructor i.e. def m1(self) will print 10
'''