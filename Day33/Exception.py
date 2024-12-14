'''
Exception handling in Python
-----------------------------
In python with the help of the exception handling concepts one can easily handles exceptions

Types of Errors
---------------
The most common errors in Python are;
1. Syntax Errors
2. Runtime Errors

1. Syntax Errors
------------------
These are errors that occur due to invalid syntax

2. Runtime Errors
------------------
When writing logic and due to memory issues this error is called runtime error
That is errors due to wrong end user input, memory problems and invalid programming logic

Who's responsible for correcting these errors?
-------------------------------------------------
1. Syntax Errors: Developers are responsible for the correction of syntax errors
After correction errors then codes will be executed

2. Runtime Errors: Exceptions handling applicable to runtime errors
'''

# Examples of SyntaxError
# -------------------------
# x = 10
# if x ==10
#     print("Hello")
'''
Output is
line 31
    if x ==10
             ^
SyntaxError: invalid syntax

Programmer is the only one permitted to correct such error
'''
# Corrected version
# x = 10
# if x ==10:
#     print("Hello")
'''
Output is
Hello
'''
# Example 2
# print "Ola"

'''
Output is 
line 51
    print "Ola"
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Ola")?
'''
# Corrected Version
# print("Ola")
'''
Output is
Ola
'''

# Examples of Runtime Errors
# ---------------------------
# 1
# print(10/2)
'''
Output ia
5.0
'''
# 2
# print(10/0)
'''
Output is
line 76, in <module>
    print(10/0)
ZeroDivisionError: division by zero
'''
# 3
# print(10/"ten")
'''
Output is
line 85, in <module>
    print(10/"ten")
TypeError: unsupported operand type(s) for /: 'int' and 'str'
'''
# 4
# reading an input from user
# input("Enter the data = ")
'''
Output is
Enter the data =
'''
# 5
# convert the string input data to integer datatype
# x = int(input("Enter the data = "))
# print(x)
'''
Output is 
Enter the data = 10
10
'''
# 6
# entering sequence of character string. String contains character not decimal value
'''
Output from second execution of the above line 101 code
Enter the data = ten
line 101, in <module>
    x = int(input("Enter the data = "))
ValueError: invalid literal for int() with base 10: 'ten'
'''
'''
"10" is string
10 is integer
"ten" is string
ten can't be converted to integer

Types of Runtime Errors
-----------------------
1. ZeroDivisionError
2. TypeError
3. ValueError
4. FileNotFoundError
5. EOFError
6. SleepingError
7. TyrePuncturedError

Runtime Errors are called Logical Errors or Exceptions
All runtime or exceptions error is an object of corresponding class
'''
# How to handle this error?
# -------------------------
print("This is starting of the program")
'''
Output is
This is starting of the program
'''
print(x)

print("This is the end of the program")
'''
Output is 
line 143, in <module>
    print(x)
NameError: name 'x' is not defined
'''