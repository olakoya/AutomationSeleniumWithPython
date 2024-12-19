# Checkout Day 21 Class_Object_Notes_3 for Class and Static Notes


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
        print(Test.b+100) # adding mathematical syntax/operation of +100
Test(10) # object accessing the testingfile value "a"
Test(20) # object accessing the testingfile value "a"
Test(30) # object accessing the testingfile value "a"
'''
Output is 
10 => printing the class variable value 'a' 
50 => printing the class variable value 'b' 
20 => printing the class variable value 'a' 
50 => printing the class variable value 'b' 
30 => printing the class variable value 'a' 
50 => printing the class variable value 'b' 

Output after adding mathematical syntax/operation +100
10
50
150
20
50
150
30
50
150

Mutiples Objects were created in the code Lines 5 to 7 and 22 to 24
Each and every object has a value arguement with repect to 'a'
In that specific constructor __init__ I'm access a variable value 'a' along with class variable 'b' created in class Test:
I created 6 objects from the above both codes which means the class is called 6 times and constructor called 6 times
Then after adding addition operator to class variable then the class got called 9 times and constructor called 9 times
Because the class variable weren't changing from the output, it simplies that for every instance the value of the variable is called
For that reason that type of variable is called CLASS VARIABLE
'''
