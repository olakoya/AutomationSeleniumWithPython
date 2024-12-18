'''
Exception Handling 3
---------------------
1. try this is ==> when we keep risky code
2. Except this is ==> when exceptions occur
3. Else this is ==> when no exceptions occur
4. Finally this is ==> when blocks are always executed

Types of Exceptions
--------------------
1. Predefined Exceptions: This is the exception that python knows
            These exceptions are raised by Python Virtual Machine PVM because of some events
            Examples are;
            ZeroDivisionError
            ValueError
            NameError
2. User-defined Exceptions or Programmatic Exceptions or Customised Exceptions: This is responsible by the user itself
            These are exceptions raised by programmer as per business requirements e.g rising keywords
            InsufficientFunds Exception
            InvalidInput Exception
            TooYoung Exception
            TooOld Exception
E.g
'''

from keyword import kwlist
print(kwlist)
print(len(kwlist))

'''
Output is
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
'raise', 'return', 'try', 'while', 'with', 'yield']
36
'''

'''
Syntax of Exceptions
---------------------
All exceptions are inherited from Parents
1. Class Classname(predefined exception class)
        def __init__(self,arg): # constructor
            self.msg = arg
E.g
'''
# Class classname(predefined exception class) # using class name defined by exception for the below codes
#         def __init__(self,arg): # constructor
#             self.msg = arg
class TooYoungException(Exception): # creating 3 young class (Exception is the parent class)
    def __init__(self,arg):
        self.msg = arg
        super().__init__(self.msg)# calling constructor by using super method with a message

class TooOldException(Exception): # creating TooYoung and TooOld objects
    def __init__(self,arg):
        self.msg = arg
        super().__init__(self.msg)

age = int(input("Enter Age = "))
if age>60:
    raise TooOldException("Please wait for some time, you will soon get the best match")
elif age<18:
    raise TooYoungException("Your age already crossed marriage age... no chance of getting marriage")
else:
    print("You will get matching details soon by email")

'''
Output is
Enter Age = 22
You will get matching details soon by email

Enter Age = 62
line 62, in <module>
    raise TooOldException("Please wait for some time, you will soon get the best match")
__main__.TooOldException: Please wait for some time, you will soon get the best match

Enter Age = 18
You will get matching details soon by email

Enter Age = 15
line 64, in <module>
    raise TooYoungException("Please wait for some time, you will soon get the best match")
__main__.TooYoungException: Please wait for some time, you will soon get the best match

Enter Age = 45
You will get matching details soon by email
'''