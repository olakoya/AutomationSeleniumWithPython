'''
Class and Object - 3
---------------------
Static Variables or Class Variables
If value of variable is constant or fixed from object to object is called STATIC VARIABLES
For total class only one copy of static variable are shared

Once an object is created, one needs to pass a parameter which is the instance variables

Declare Static Variables
-------------------------
1. In general we can declare within the class directly but from outside of any method
2. Inside constructor and method by using class name
3. Inside classmethod by using either class name or cls variable
4. Inside static method by using class name
5. Outside of class by using class name

Inside a constructor and method if we are having any class variables then to declare, it's either we need to create an object 
or we need to explicitly call the method otherwise, the variables won't be declared as class variables.

Class variables are static variables. For each of every object there is a single copy of class variable.

To understand how many copies of class variable is created one need to access the class variable.

Access Class Variable
-----------------------
1. Inside constructor by using either self or classmate
2. Inside instance method by using either self or classname
3. Inside class method by using either cls variable or classname
4. Inside static method by using classname
5. From outside of class by using either object reference or classname

Out of all the access listed above what the have in common in CLASSNAME
It is advisable to always go with the classname wherever we declare class variable

'''