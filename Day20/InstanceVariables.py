'''
Instance Variables
--------------------
They are nothing but an object. (Variable is a memory that stores data)
Example is a user name or age in an user profile
One can capture datas inside variable and that variable becomes instance variable
If the value of the variable is changing from instance to instance it then becomes INSTANCE VARIABLE
For every object a separate copy of instance variables are created

HOW MANY WAYS CAN WE DECLARE INSTANCE VARIABLES?
Declaration of Instance Variables
----------------------------------------
1. Inside constructor by using self variable
2. Inside Instance method by using self variable
3. Outside of the class by using object reference variable

'''



class Test:
    def __init__(self,a,b): # self, a, b are parameters
        self.a = a # inside the constructor we are using the a and b values of the parameters
        self.b = b # a and b parameters can also be written in numbers like 10 and 20
        # and to make it instance variable we would add "self" = to each of the parameters
        # defining any variable with "self" will automatically becomes INSTANCE VARIABLE
        # we also use the same parameter names a and b to declare the instance variables by 
        # adding .a and .b or .x and .y with the help of "self" in lines 22 & 23
Test(10,20) # passing values (a=10,b=20) to parameters and adding reference "t" to object
Test(100,300) # since the inputs of the parameters are changing it becomes INSTANCE VARIABLES
Test(44,67) # the values of the parameters are chaing from object to object, its called instance variable

class Test:
    def __init__(self,a,b): 
        self.x = a
        self.y = b

    def m1(self):
            c = 30
            print(self.x+self.y+c)

t1 = Test(10, 20)
t2 = Test(200, 300)
t3 = Test(34, 25)
t1.m1()
t2.m1()
t3.m1()