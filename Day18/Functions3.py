'''
Lambda Functions or Anonymous Functions or Nameless Functions
---------------------------------------------------------------
These are functions without a name. They are very impotant functions.
When one wants to implement a big task, one doesn't need to write a big statement like that of TypesofVariableFunctions file in Day 17.
With Lambda one can create a single statement without a name.
A lambda function is an anonymous function.

Lambda Syntax
---------------
1. Lambda ==> "lambda" is the keyword that will be used just as def is used in the previous files and its compulsory
2. lambda arguement_list ==> "arguement_list" in this code is the parameter
3. lambda arguement_list : expression ==> ": expression" will return some results
4. There is no name specify for this lambda function which makes it a nameless lambda function
5. This code can only be used for a one-time task
6. This is a concise code meaning in the code we can only write one single statement
7. By default lambda function will return a result upon executeing the ":expression" function
'''
# E.g
# Print a square of Number
# A Normal Function
# -------------------

# def squareit(n): # Using a "def" keyword with a function name "squareit" including an open and close parenthensis ()
#     print(n*n) # and inside the body I'm specifying the expressions (n*n) by accepting some parameters

# squareit(3)
# squareit(10)
# squareit(300)
'''
Output is 
9
100
90000
'''

'''
Lambda Function
----------------
To define a lambda function one needs to specify a lambda keyword
lamba ==> Once the lambda keyword has been defined one need to specify the arguement list
n: ==> This is the arguement list and for that reason we are using only a parameter to get THE SQUARE OF A NUMBER just as the above example code
n*n ==> This is the expression one will print
n,m ==> This is to have and to specify double arguement but for lambda it is only one arguement or expression we need
s ==> This is assigning a variable should there be any changes in data so as to be stored in this lambda n:n*n function
Then we can print the variable with the help of the arguement
'''
# E.g
# s = lambda n:n*n
# print(s(4)) # without the print statement it will be impossible to see what the expression is returning to me
# print(s(100))
# print(s(1000))
'''
Output is
16
10000
1000000

Lambda function is a simple or one-time task 
It is also used as an arguement to another function and these are the following types below;

Types of Lambda Function
------------------------
1. filter() function ==> this filter the data
2. map() function ==> this applies function to each and every element of a sequence which simplify the logic and return a result
3. reduce() function 

Most of the time lambda function is used as an arguement to the above 3 functions and the above 3 can be a function to another arguement
Lets look at how we can reach an requirement with the help of the 3
'''
'''
Filter Function
----------------
This will filter values from given sequence if the sequence is a requirement.
The logic to filter inside sequence is taken from lambda function
This filter function takes another function as an arguement
It will specify the logic and based on that it will filter the values in sequence
Example of Sequence are string, list, tuple,set, dictionary, range etc. 
Whenever sequence is mentioned, one of the examples should come to mind
    syntax ==> filter(function, sequence)
Out of the sequence is to print a data based on condition and the condidtion is based on function
And once the arguement is passed through the filter function it will filter the value from the sequence
'''

# Filter() Function
# ------------------------
# E.g 1 divisible by
# i = [0,5,10,15,20,25,30] # List of sequence
# # From the list we need to filter value and to print them visible by 2 one needs to use the filter function
# print(list(filter(lambda x:x%2==0,i)))
# lambad is an arguement list and needs to make it visible by 2
# Expression is making the sequnce divisible by 2
'''
"i = [0,5,10,15,20,25,30]" is List of sequence
"filter" is a function taking another function 
"lamba" is a keyword followed by "x" arguement key (i.e "lambda x" as an arguement)
Then followed by ":x%2==0" a colon expressions
In this simple line "lambda x:x%2==0", one is achieving this function and specifying a logic
"x" is taking an arguement from this i = [0,5,10,15,20,25,30] sequence individual number
"x%2" this is filtering the value which is divisible by 2 with an i i.e a number from the sequence is divided by 2
"print(list)" And to print it's converted to data structure in the form of list result

Output is 
[0, 10, 20, 30]
'''
# E.g 2 not divisible by 2
# i = [0,5,10,15,20,25,30]
# print(list(filter(lambda x:x%2!=0,i)))
'''
Output is 
[5, 15, 25]
The function contains some logic
'''

# Map() Function
# ------------------------
# E.g 1 addition of 2
i = [0,5,10,15,20,25,30]
print(list(map(lambda x:x+2==0,i)))
'''
Output is 
[False, False, False, False, False, False, False]
'''