a = 10 # a is an assignment operator for 10
b = 2 # b is an assignment operator for 2

print(a>b) # Output is True
print(a<b) # Output is False
print(a>=b) # Output is True
print(a<=b) # Output is False

# "Print" statement should always be use if it's returning a value
# When one condition is True the other is False
"""
With the above scripts one can derive a relationship approach with integer and string
They can be al types of data, either integre, boolean, or string
"""

# Coomparision on strings is based on ascii code e.g
a = "John" # strings
b = "Ram"
print(ord('J')) # 74
print(ord('R')) # 82

print(a>b) # Output is False
print(a<b) # Output is True
print(a>=b) # Output is False
print(a<=b) # Output is True

# Comparision on strings is based on ascii code
print(ord('J')) # character and acsii code is "74"
print(ord('R')) # character and acsii code is "82"

# Boolean values shouldn't be spicify in a string
# Boolean value for True is 1
# Boolean value for False is 0
print(True > True) # Output is False
print(True >= True) # Output is True
print(10>True) # Output is True
print(False > True) # Output is False
print(10>"True") # Output is TypeError because '>' not supported between instances of 'int' and 'str'
# The above scripts is doing comparision between integers, strings and boolean datatypes

# Chaining of relational operators is possible
print(10<20<30<40>50) # Output is False because 40 isn't greater than 50
# this is using relational operators but between different values which is called chaining
# Any operators can be used for Chaining. It can be either Equality or Comparision operators.
# Equality always performs content comparison
# If at least one comparison returns False then the result
x = 5 # equals 5
x == 10 # this is comparing the content ie. 5 and 10
x != 10 # not equal to 10