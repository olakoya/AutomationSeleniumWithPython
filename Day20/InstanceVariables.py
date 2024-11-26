class Test:
    def __init__(self,a,b): # self, a, b are parameters
        self.a = a # inside the constructor we are using the a and b values of the parameters
        self.b = b # a and b parameters can also be written in numbers like 10 and 20
        # and to make it instance variable we would add "self" = to each of the parameters
        # defining any variable with "self" will automatically becomes INSTANCE VARIABLE
        # we also use the same parameter names a and b to declare the instance variables by 
        # adding .a and .b or .x and .y with the help of "self" in lines 3 & 4
Test(10,20) # passing values (a=10,b=20) to parameters and adding reference "t" to object
Test(100,300) # since the inputs of the parameters are changing it becomes INSTANCE VARIABLES
Test(44,67) # the values of the parameters are chaing from object to object, its called instance variable