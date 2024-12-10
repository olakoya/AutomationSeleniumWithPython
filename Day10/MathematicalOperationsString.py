'''
Mathematical Operations on String
----------------------------------
It contains two types
1. Cancatenation means ==> + ==> another word is combining
2. Repitition ==> * ==> repition of string

E.g
'''
a = "Hello"
b = "World"
# to combine the above two strings together, what to use is Cancatenation

print(a+b)
'''
Output is
HelloWorld
'''
# E.g 2
# x = 2 # integer
# y = "World" # string

# print(x+y)
'''
Output is
TypeError: unsupported operand type(s) for +: 'int' and 'str'

The above execution is impossible because integer and string cannoy be combined together
'''

'''
If we want to compulsorily use concatenation operator, both arguements must be of the same data type
E.g
'''
print("Hello" + "World")
'''
Output is
HelloWorld
'''
c = "Ola"

print(c*10)
'''
Output is
OlaOlaOlaOlaOlaOlaOlaOlaOlaOla
'''
# print(a*b) # a = "Hello", b = "World"
'''
Output is 
TypeError: can't multiply sequence by non-int of type 'str'

To compulsorily use repitition operator, one arguement must be of integer and other must be string datatype
'''
#-----------------------------------------------

# Count of Characters
# ---------------------
a = "welcome"
print(len(a))
'''
Output is
7
'''
#--------------------------------------------------

# Membership Operators ==> in and not in ==> This is use to checking presence of an object in a sequence
# ------------------------
d = "welcome"

print("z" in d)
print("z" not in d)
'''
Output is
False
True
'''
print("l" in d)
print("l" not in d)
'''
Output is
True
False
'''