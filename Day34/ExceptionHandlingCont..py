'''
Exception Handling
-----------------
Most common errors are;
1. Syntax Errors
2. Runtime Error ==> Exceptional Error

How to Handle the Errors are
1. Try Block
2. Except Block

Based on the 2 handling Errors above, it's important thing to know the below for the Errors;
!. Any code which causes exception us called a Risky code
    The risky code can be placed/kept inside Try block
2. If exception handling code specify except block
E.g
'''
print("this is the starting of the program")
try: # when try block is used "except" block is use as a default
    # print(x) # accessing variable and a line block of risky code
    print(10 / 0)
except:
    print("Exception occurred")
print("this is the end of the program")
'''
Output is 
line 19, in <module>
    print(x) # accessing variable
NameError: name 'x' is not defined (and)
this is the starting of the program

(The statement after an error can't be executed hence executing only line 18)

Output after adding lines 19, 21, 22

this is the starting of the program
Exception occurred
this is the end of the program
E.g 2
'''
print(10/0)
'''
Output is
line 40, in <module>
    print(10/0)
ZeroDivisionError: division by zero

Moving line 40 to line 21

Output gives

this is the starting of the program
Exception occurred
this is the end of the program

E.g 3
'''
try:
    x = int(input("Enter 1st Number: "))
    y = int(input("Enter 2nd Number: "))
    print(x/y)
except
'''
Output is
Enter 1st Number: 10
Enter 2nd Number: 20
0.5

Enter 1st Number: 15
Enter 2nd Number: 0
line 60, in <module>
    print(x/y)
ZeroDivisionError: division by zero

Enter 1st Number: 10
Enter 2nd Number: ten
line 59, in <module>
    y = int(input("Enter 2nd Number: "))
ValueError: invalid literal for int() with base 10: 'ten'

As I use 'try' and 'except' blocks to handle exceptions in this case one can specify different types of errors
The above code can cause;
Different Type of Errors
-------------------------
i. ZeroDivisionError
ii. ValueError

E.g 4
'''
try: # using try block
    x = int(input("Enter 1st Number: "))
    y = int(input("Enter 2nd Number: "))
    print(x/y)

except ZeroDivisionError: #using exception block because the code can also cause exception
    print("Cannot divide by Zero")

except ValueError:
    print("Please provide an integer value only")

except:
    print("Exception Occurred")
'''
Output is
Enter 1st Number: 10
Enter 2nd Number: ten
Please provide an integer value only

Enter 1st Number: 20
Enter 2nd Number: 0
Cannot divide by Zero

E.g 5
'''
try:
    x = int(input("Enter 1st Number: "))
    y = int(input("Enter 2nd Number: "))
    print(x/y)

except (ZeroDivisionError, ValueError):
    print("Please provide valid data")

except:
    print("Exception Occurred")
'''
Output is
Enter 1st Number: 20
Enter 2nd Number: 0
Please provide valid data

Enter 1st Number: 10
Enter 2nd Number: 2
5.0

E.g 6
'''
try:
    x = int(input("Enter 1st Number: "))
    y = int(input("Enter 2nd Number: "))
    print(x/y)

except (ZeroDivisionError, ValueError) as msg: # as is an alias
    print("Please provide valid data", msg)

except:
    print("Exception Occurred")
'''
Output is
Enter 1st Number: 10
Enter 2nd Number: 0
Please provide valid data division by zero

Enter 1st Number: 10
Enter 2nd Number: ten
Please provide valid data invalid literal for int() with base 10: 'ten'

Enter 1st Number: 81
Enter 2nd Number: 9
9.0

Enter 1st Number: 100
Enter 2nd Number: 3
33.333333333333336
'''
'''
Aside from 'try' and 'except' blocks, blocks that can also be used are;
iii. finally which is always ==> executed. 
        finally is also use as a clean up code
    Example is that after automating a test case that requires the database and after automation database is disconnected that's
    what is called clean up code
iv. else which is when no exceptions ==> occurred

E.g
'''
try:
    print(10/2)
except:
    print("Exception Occur")
finally:
    print("Always executed")
'''
Output is for 10/0
Exception Occur
Always executed

changing code line 174 from 10/0 to 10/2
Output is
5.0
Always executed

E.g 2
'''
try:
    print(10/0)
except:
    print("Exception Occur")
else:
    print("No exceptions Occurred")
finally:
    print("Always Executed")
'''
Output is
5.0
No exceptions Occurred
Always Executed

But switching code line 192 from 10/2 to 10/0
Output is 
Exception Occur
Always Executed

E.g 3
'''
import os
try:
    os._exit(0)  # this is a protected member i.e when execution gets to this line it's get shutdown
    print(10/0)

except:
    print("Exception Occur")
else:
    print("No exceptions Occurred")
finally:
    print("Always Executed")
'''
Output is blank

Except blocks only execute when there is some exceptions i.e
i. Except block ==> executes only when exception occurs
ii. Else block ==> executes only when exception isn't occurred
iii. Finally block ==> executes always
'''