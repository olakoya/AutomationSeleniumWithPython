# Checkout Day 19 Class_Object_Notes for Class, Methods and Object Notes

class Test: # created inside a class and outside a method
    x = 10 # class variable (created in a class and outside a constructor)
# In general we can declare within the class directly but from outside of any method
    def __init__(self):
        self.y = 20 # instance variable
        Test.z = 30 # class variable

    def m1(self):
        Test.l = 40 # class variable => Inside constructor and method by using class name

    @classmethod
    def m2(cls): # => Inside classmethod by using either class name or cls variable
        Test.k = 50 # class variable 
        cls.m = 60 # class variable => Inside static method by using class name
# every method that has been written under "class Test:" as seen above regardless of there def function name are all members of "class Test:" class
# To see the members of the class at once, one needs to use the "Test.__dict__" method ie "Test dictionary constructor" function
# "Test.__dict__" this will display the method in the form of a dictionary without calling each and every method individually
# With a print function it will return result from all the method together instead of one by one execution

print(Test.__dict__)
'''
Output is
{'__module__': '__main__', 'x': 10, '__init__': <function Test.__init__ at 0x1005a93a0>, 'm1': <function Test.m1 at 0x1005a9620>,
 'm2': <classmethod(<function Test.m2 at 0x1005a98a0>)>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': 
 <attribute '__weakref__' of 'Test' objects>, '__doc__': None}

 The above result means:
 1. There is a variable x = 10 => '__module__': '__main__', 'x'
 2. I have a constructor __init__ => '__init__': <function Test.__init__ at 0x1005a93a0>,
 3. I have a method m1 => 'm1': <function Test.m1 at 0x1005a9620>,
 4. I have another method m2 => 'm2': <classmethod(<function Test.m2 at 0x1005a98a0>)>,
 5. I have a dictionary constructor __dict__ => '__dict__': <attribute '__dict__' of 'Test' objects>,
 6. And weak reference constructor __weakref__ => '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
 7. Then these are the members of this particular "class Test:" class => 'x': 10, '__init__': <function Test.__init__ at 0x1005a93a0>, 
    'm1': <function Test.m1 at 0x1005a9620>, 'm2': <classmethod(<function Test.m2 at 0x1005a98a0>)>, 
So the reason why these  self.y = 20 # instance variable and Test.z = 30 # class variable weren't executed is because object wasn't 
created even though that __init__ constructor does execute automatically.

We only print "print(Test.__dict__)" the members of the class in form of key value

So to print (self.y = 20 # instance variable and Test.z = 30 # class variable) we need to create an object "Test" of the class and use a
"t" reference to call it (like building and house and giving it an address) and print it with the dictionary constructor __dict__

'''
t = Test()
print(Test.__dict__)
'''
Output is
{.....'__module__': '__main__', 'x': 10, '__init__': <function Test.__init__ at 0x1063f53a0>, 'm1': <function Test.m1 at 0x1063f5620>,
 'm2': <classmethod(<function Test.m2 at 0x1063f58a0>)>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': 
 <attribute '__weakref__' of 'Test' objects>, '__doc__': None} {'__module__': '__main__', 'x': 10, '__init__': <function Test.__
 init__ at 0x1063f53a0>, 'm1': <function Test.m1 at 0x1063f5620>, 'm2': <classmethod(<function Test.m2 at 0x1063f58a0>)>, 
 '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__'
 : None, 'z': 30}

In this case have ( 'z': 30) at the end because "z" is a class variable, and it's present in the __init__ constructor

Once we use print(Test.__dict__) dictionary constructor, it displays the class member
Previous output didin't display the members of the class but once we created the instance class (t=Test) it's declare the 
class variable then we could see the output of class variable as "z = 30" inside the output dictionary

So, with the help of the print object variable (print(Test.__dict__)), I will call a method (t.m1()) with adding (print(Test.__dict__)) 
below it and after calling (def m1(self): Test.l = 40), inside of the method we have class variable (Test.l = 40)
'''
t.m1()
print(Test.__dict__)
'''
Output is 
{.... None, 'z': 30, 'l': 40}

I just called the method t.m1() and print(Test.__dict__) to achieve the above "'l': 40" output
'''
t.m2()
print(Test.__dict__)
'''
Output is below after calling the t.m2() method using the object reference variable. Both class variables in the method were displayed
{.....None, 'z': 30, 'l': 40, 'k': 50, 'm': 60}

By so doing one can create class variable by using the DECLARE STATIC VARIABLES as seen in the Class_Object_Notes_3 file

But by default, once a class variable is created outside of a method inside a class it's available but inside the constructor 
there's a variable however, inside the m1 method and classmethod-m2 method I have another class variable.
These variable can be initialised as class variable once I create an object and call their particular method then it becomes class variable

'''
Test.n = 70 # class variable => Outside of class by using class name
print(Test.__dict__)
'''
{....None, 'z': 30, 'l': 40, 'k': 50, 'm': 60, 'n': 70}
Because it is a class name it's printed inside the class Test: class dictionary
'''

# INSTANCE VARIABLE
# ------------------

class Test:

# defining a simple class using just one way below
    a = 10 # class variable
    def __init__(self):
        print(Test.a) # using "Test" as class name and the same data Test.a

    def m1(self): # inside constructor I'm accessing the instance method m1 
        print(Test.a) # inside the method I'm using the same approach

# defining a method and Inside class method by using either cls variable or classname
    @classmethod
    def m2(cls): # defining a class method with cls
        print(Test.a) # with the help of class name "Test" and with the help of cls I can access the class variable "a = 10"

# defining another method using static method / Inside static method by using classname
    @staticmethod
    def m3(): # defining static method with an empty parentheses 
     print(Test.a) # printing class variable ie printing the value of the variable

# creating testingfile objects / From outside of class by using either object reference or classname
# Create an instance of Test
t = Test() # Should print: 10 (from __init__) => Calls the constructor, prints 10
# Calling all the method with the help of object reference variable
# Call m1 (instance method)
t.m1()
# Call m2 (class method)
t.m2()
# Call m3 (static method)
t.m3()
print(Test.a)
'''
Outputs are
10  # From __init__
10  # From m1
10  # From m2
10  # From m3
10  # From Test.a
'''