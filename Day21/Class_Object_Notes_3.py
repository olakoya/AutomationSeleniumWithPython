'''
Class and Object - 3
---------------------
Static Variables or Class Variables
If value of variable is constant or fixed from object to object is called STATIC VARIABLES
Then we can create that variable inside a class but out of a method/constructor
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

Access Class/Static Variables
------------------------------
1. Inside constructor by using either self or classmate.
2. Inside instance method by using either self or classname.
3. Inside class method by using either cls variable or classname.
4. Inside static method by using classname.
5. From outside of class by using either object reference or classname.

Out of all the access listed above what they have in common in CLASSNAME.
It is advisable to always go with the classname wherever we declare class variable.

We use classname for declaration and accessing inside and outside of a class
'''

'''
Local Variable
---------------
1. It is sometimes use to meet temporary requirements of programmer, one can declare variables inside a method directly.
Those types of variables are called local variable or temporary variables.
2. Local variables will be created at the time of method execution and destroyed once method completes.
3. Local variables of a method cannot be accessed from outside of method.
4. Example of local variable is storing intermediate results in a calculation.
5. Local variables only respond to the function and to store in local 
6. Before completing the execution of a program one will get a result and to store the result one needs a temporary requirements
7. To meet temporary requirements programmers declare a variable inside a method without self/class name
'''