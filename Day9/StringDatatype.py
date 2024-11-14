'''
String Data Type in Python:
---------------------------
A string is a sequence of character enclosed with double or single quotes.
E.g
name = "John" # each letter in John is a character in string datatype.
Any data in double or single quote is a string.
Inside single quotes we should never use single quotes likewise in double quotes in double quotes
They are invalid syntax
However, we can use double quotes inside single quotes likewise in single quotes in double quotes
'''

# Create a String
# ---------------
s = "welcome" # anything in the quote is called string
s = 'welcome' # welcome is a sequence of character
'''
's' is a variable  stored in a type ()
type( ) is like a method and once you pass a variable to the method one can know what class it is
() type is a class e.g type(object) i.e. object's type
type(name, bases, dict, **kwds(keywords)) => a new type
# (copied from class doc)
If anything i.e. a method is written in python and to see the statement we use 'print' statement e.g print(type(s))
'''
s = " " # space inside quotes is classied as string datatype
s = ' ' # space inside quotes is classied as string datatype
s = 123 # this data is treated as integer datatype since it's not located inside quotes
s = "123" # any data inside quotes is classied as string datatype
s = str(123) # this is called type casting and the integer is coverted to string by adding str() datatype

print(type(s)) # <class 'strg'>

# Multiple line string Literals
# ----------------------------

s = " Learning Exchange"
s = '''Learning
Exchange
'''
s = """ Listening
in
Class
"""
print (s)

# single and double quotes

# s = "This is "string data" type introduction session day"

'''
Output is 
s = "This is "string data" type introduction session"
                  ^^^^^^
SyntaxError: invalid syntax
'''

s = "This is 'string data' type introduction session"
s = "This is \"string data\" type introduction session day"
print (s)

'''
\ ==> escape character:
Second or ending (', ") quote is called terminate quote
We can use double quotes inside single quotes likewise in single quotes in double quotes e.g
"This is 'string data' type introduction session"
'''

'''
\ ==> Escape Character

Accessing Characters inside String
-----------------------------------
s = "welcome" 
s = "Hello"

Types are:
----------
Index 
Slice operator

Every character inside string will have address or location or index.
With the help of address or location or index we can access data inside a string.
E.g
s = "welcome" (w e l c o m e ) in the string are all individual character that has an address or location

Accessing characters by index
------------------------------
Python support both +ve and -ve indexing
+ve and -ve characters are called index

0   1   2   3   4
H   E   L   L   O
-5  -4  -3  -2   -1

+ve ==> (L to R) ==> forward direction

-ve <== backward direction <== (R to L)

In the forward direction ==> the first index is "0" for the "H" character as seen from above
'''