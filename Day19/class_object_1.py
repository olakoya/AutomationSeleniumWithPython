'''
class class_name: # class creation
                "documentation string"
                variables
                methods
        
        class name() # class calling => object of a particular class
'''
# creation of a class

class Test: # class creation
    a = 10 # class variables
    def test(self): # function created in a class is called method i.e creating a method and test name is test
        print(self.a) # this is accessing the class variable # "self" is helping to access

t1 = Test() # object
t2 = Test() # object
t3 = Test() # object
t4 = Test() # object
t5 = Test() # object
t6 = Test() # object
t7 = Test() # object

print(t1.a) # to see a data present in "a = 10", print will help in accessing the variable "a" with the object "t1"
t1.test() # we are accessing an object "t1.test()" with the help of "print(t1.a)" and print out the value in a = 10
print(t2.a)
t2.test() 

'''
Output is
10
10
10
10
'''

'''
Explanantion of the codes above
--------------------------------
Inside "class Test:" this "def test(self):" is defined i.e. 
To say "def test(self):" is a property of this "class Test:" we need to use the "self" parameter
And "self" is a mandatory parameters
Once it's created we need to specify this "def test(self):" otherwise one would get an error
And when a class variable "a = 10" is created one can access it through "print(self.a)"
To make our class physically appeared we need to create an object "Test" with open close parentheses
For instance in building a house we need to design it before construction
Therefore designing of the house in this instance is class method while construction is the test() object
For single class we can create any total number of objects
Once a class is created we can create many number of objects and this objects are independent
Which means with a single design we can construct many number of houses from that one design 
And all these houses are stand alone and independent despite having the same design
Then through these objects (Test()) they can have different reference variables (t1 = ) i.e. all these houses will have different addresses
With the help of the reference (t1 = ), one can access the variable (a = 10) and method of the class
To see a data present in "a = 10", print will help in the access of variable "a" with the object "t1"
We are accessing an object "t1.test()" with the help of "print(t1.a)" and print out the value in a = 10
With the help of "t1.test()" we are calling the method "print(self.a)"
'''