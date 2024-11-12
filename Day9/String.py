'''
String Data Type in Python:
---------------------------

Any data...

Inside single quotes we should never use single quotes likewise in double quotes in double quotes
They are invalid syntax
However, we can use double quotes inside single quotes likewise in single quotes in double quotes
'''

# Create a String
# ---------------
s = "welcome" # anything in the quote is called string
s = 'welcome'
s = " "
s = ' '
s = 123
s = "123"
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

'''