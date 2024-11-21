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

def squareit(n): # Using a "def" keyword with a function name "squareit" including an open and close parenthensis ()
    print(n*n) # and inside the body I'm specifying the expressions (n*n) by accepting some parameters

squareit(3)
squareit(10)
squareit(300)
'''
Output is 
9
100
90000
'''