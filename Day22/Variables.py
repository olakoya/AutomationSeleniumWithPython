class Test: # defining a class
    def __init__(self,a): # definig a constructor and inside of it is a parameter called  "self" and pass a parameter "a" called arguement 
                            # making 'a' an instance variable
        print(a) # then we print the parameters 'a', (__init__) is a function passing parameter to 'a'
Test(10) # creating an object from instance variable as it changes
Test(20) # creating an object from instance variable as it changes
Test(30) # creating an object from instance variable as it changes
# once an object is passed the constructor will automatically work or be executed
'''
Output is 
10
20
30
'''

class Test:
    b = 50 # b is a class variable and also constant located out of a constructor class
    def __init__(self,a):
        print(a)
        print(self.b) # print the b value
Test(10) # object accessing the test value "a"
Test(20) # object accessing the test value "a"
Test(30) # object accessing the test value "a"
'''
Output is 
10 => printing the class variable value 'a' 
50 => printing the class variable value 'b' 
20 => printing the class variable value 'a' 
50 => printing the class variable value 'b' 
30 => printing the class variable value 'a' 
50 => printing the class variable value 'b' 
'''
