'''
Lambda Functions or Anonymous Functions or Nameless Functions
---------------------------------------------------------------
These are functions without a name. They are very impotant functions.
When one wants to implement a big task, one doesn't need to write a big statement like that of TypesofVariableFunctions file in Day 17.
With Lambda one can create a single statement without a name.
A lambda function is an anonymous function

Lambda Syntax
---------------
1. Lambda ==> lambda is the keyword that will be used just like def is used in the previous files and its compulsory
2. lambda arguement_list ==> arguement_list is the parameter
3. lambda arguement_list : expression ==> : expression will return some results
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
n*n ==> And this is the expression one will print
n,m ==> This is to have and specify double arguement but for lambda it is only one arguement or expression we need
s ==> This is assigning a variable should there be any changes in data so as to be stored in this lambda n:n*n function
Then we can the variable with the help of the arguement
'''
# E.g
s = lambda n:n*n
print(s(4)) # without the print ststement it will be impossible to see what the expression is returning to me
print(s(100))
print(s(1000))
'''
Output is
16
10000
1000000

Lambda function is a simple or one-time task 
It is also used as an arguement to another function and these are follows below;

Types of Lambda Function
------------------------
1. filter() function ==> this filter the data
2. map() function ==> this applies function to each and every element of a sequence which simplify the logic and return a result
3. reduce() function 

Most of the time lambda function is used as an arguement to the above 3 functions
'''