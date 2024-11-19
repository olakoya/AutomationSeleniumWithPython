'''
Functions in Python
--------------------
1. If a group of statements is repeatedly required then it is not recommended to write these statements everytime seperately.
E.g
The below 3 code statements aren't required and they are all doing the same addition statements;
'''
a = 10
b = 5
print(a+b)
'''
Output is 15
'''
c = 100
d = 250
print(c+d)
'''
Output is 350
'''
e = 79
f = 47
sum = e+f
print(sum)
'''
Output is 126

We do have duplications and maintenance issues following the above codes
'''
'''
2. We have to define these statements as a single unit and we can call that unit any number of times based on our requirements 
without rewriting the code. This unit is nothing but functions.

3. The main advantage of functions is for code relaibility and to avoid duplication.

4. In other languages functions are known as methods, procedures, subroutines etc.

5. Function and Method are different in python.

6. After learning this function it will be easy to understand Object Oriented Programming (OOP) Language
'''

'''
Furthermore, Function is a group of statements upon calling. Calling it will perform certain task or operation.

Types of functions
-------------------

1. Built-in functions
----------------------
Comes along with python software
    print(), id(), type(), eval(), etc

2. User-defined functions
--------------------------
E.g 
a. In a project during implementation phase there will be different logic as per the requirements
b. Depending upon the business requirements if we develop a function, the function is called 'User-defined functions'
c. User means Developer
d. Developers define some functions according to the business requirements and this is called 'User-defined functions'

Syntax of User-Defined Functions
---------------------------------
a. Most of the time we will create methods whenever we are implenting a Page Object Model.
b. And this Page Object model is a method which is a function created in a class.
c. If you know the function it's easy to work with a class and object because inside classes there is a method.
d. To create a method we need to know how to create a function:
e. And to create function we need to follow the below steps:
    1. we need to know how to use 'def' keyword. ==> def
    1a. Def is a declaration or creation of a function
    2. Afterwards, we need to specify a function name ==> def function_name
    3. Then we need to specify the open and close parenthesis () ==> def function_name(inputs/parameters)
    4. And then we specify colon : ==> def function_name():
    5. The above syntax is how we can create a function
    6. once we specify the function, directly under it i.e. function_name comes:
        def function_name():
            i. in some cases we can specify documentation string ("""doc string""") in double quotes " "
            i.e. comments telling what the above line of code (function_name) is going to do.
            ii. there can be group of statements inside the function body (ie the statement is placed directly underneath function_name)
            iii. it will try to return some datatype i.e. return result or not return result
            iv. what this function_name is going to do will be described or specify by 'doc string' 
            v. And this function_name can also have parameters
            vi. parameters are nothing but inputs and can be as many as it's required
            vii. add_element() is calling or invoking a function

Example of User-Defined Functions are:
-------------------------------------
    def add_element(a,b):
    sum = a+b
    print(sum)

Find the live code and explanantion below;
'''

def add_element(a,b): # Declaration or creation of a function
    sum = a+b # sum/adding of the parameters
    print(sum)

add_element(10,5) # parameters turned arguements after adding values
add_element(100,250)
add_element(79,47)
# Group name is called a function name
'''
Outputs are:
15
350
126
Outputs are called Values
'''
'''
Above codes explanation:
-------------------------
1. Line 89: def add_element(a,b): ==> This is a call declaration
2. add_element ==> This is a function call
3. (a,b) ==> This function is accepting two parameters a and b
4. If the function (a,b) is accepting some input, Parameters are nothing but input
5. Whenever you are calling a function 'add_element', you need to specify values to these parameters (a,b)
6. The number 5. above action is called arguement
7. But parameters are different call to that of arguement call
8. If you provide value to the input (a,b) i.e to the parameter it then becomes arguement
9. Line 93: After that a function is called 'add_elements()', then a value will be added to this line of parameters
10. Line 93:Adding value to 'add_elements(a:10, b:5)' therefore, 10 and 5 are called arguements which is values to the input (a,b)
11. Line 94 and 95: For this step the the function body 'sum = a+b' and 'print(sum)' which is also called group of statements are executed
12. Line 90: The same value '10 and 5' will come into the body of statement 'sum = 10+5' to replace 'a+b'
13. Line 91: It will then be printed in the console
14. Line 94 to 95: This line of code will keep calling the function
15. We are only calling the group name 'add_element' with arguement'(10,5)' which is nothing but a function and this is repeated on Line 94 and 95 
16. And Number 11 method is being called again and again for Line 94 and 95 as it was in the previous first 3 repititive group statements at the beginning of this page

'''
'''
What are the mandatory Parameters?
-----------------------------------
1. def
2. function_name
3. Open and close parenthesis ()
4. colon :
5. Inside body we have group of statements (sometimes we can define empty functions) which is optional
6. Result, and this can be optional too
7. Parameters are also optional
8. Inputs/Parameters are nothing but inputs to the function. (This input means it's asking or requesting for something which is data)
9. Inputs/Parameter (a,b) calling function_name
10. Values are added for a and b during function add_elements() calls 
11. And after adding values to parameters it becomes arguements during function calls
12. Parameters are inputs to the function call and values are arguement to the parameters
'''
'''
There are 4 Scenarios to these functions based on Inputs/Parameters;
---------------------------------------------------------------------
1. No Arguements and No Return Value or Result
2. With Arguements and No Return Value or Result
3. With Arguements and With Return Value or Result
4. No Arguements and With Return Value or Result
'''
'''
Types of Arguements
--------------------
1. Positional
2. Keyword
3. Default
4. Variable Length
5. Keyword Variable Length

'''