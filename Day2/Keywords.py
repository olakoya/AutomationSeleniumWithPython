'''
Reserved words or Keywords
- Represent some meaning or functionality
- There are 35 reserved words
- Keywords are also called reserved words
- To see how many reserved words are available we need to import the keyword module e.g the code below

'''

import keyword # keywords are nothing but modules
# Inside the above module keyword we have multiple reserved words or multiple keywords

print(keyword.kwlist) # keyword retuned list of keyword(kw)

'''
Output (['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
)
'''

'''
The execution returned me a list of data structure. 
The above list are multiple elements represented in sqaure brackets, seperated by commas and created as a list of data types.
'''

'''

The above Keywords represent some functionality in python and they are 35 of them and they are boolean list
Def is a specific word only meant for creating a function
Def should never be use for creating keyword for creating a variable

'''
print(len((keyword.kwlist))) 
# this is to get the count of elements from the lenght and this can be applied by the length of the function 
# # And this will return the count of elements, objects, items present inside the list and print will output the total number of keywords
# We have 35 total words
# These keywrods will be used extensively 
# Keyword "Import" is to import a model

'''
Another example of keyword is "from keyword import kwlist"
We can see from above that we have two keywords "from" and "import" from the 35 keywords list
This is one way of importing classes and models available inside a package 
E.g
'''
from keyword import kwlist 
print(kwlist)
print(len(kwlist))

'''
We have a dedicated concepts on how to import keywords and packages
Above is a multiple ways of importing from keywords
We need to understand variables
'''