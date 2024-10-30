print (10==20) # Output is False, which means a false boolean value 
print (10!=20) # Output is True, which means a true boolean value 
print (10==True) # Output is False, which means a false boolean value 
print (False==False) # Output is True, which means a true boolean value
print ("John"=="John") # Output is True, which means a true boolean value
# The above are comparing the content if they're equal, and this is called equality operators

# Operator Type : Equality Operators
# Operators and Descriptions: 
#1. == Equal
#2. != Not Equal

# Above is a true boolean value
# Chaining concept is applicable for equality operators. If at least one comparison returns False then the results is False.
# Otherwise it is True.

x = 5
x == 10
x != 10

print(10==20==30==40) # Output is False, which means a false boolean value 
print(10==10==10==40) # Output is False, which means a false boolean value 

# Operator Type: Logical Operators
# Opeartors: and, or , not (not is just a compliment)

# a-True, b-True, a and b-True, a or b-True, not a-False
# a-True, b-False, a and b-False, a or b-True, not a
# a-False, b-True, a and b-False, a or b-True, not a-True
# a-False, b-False, a and b-False, a or b-False, not a-

# We can apply logical operators on all data types

# For Boolean Data Type
#       and => If both arguements are True then it is True
#       or => If atleast one arguement is True then result is True
#       not (!=) => Complement is if one arguement is False it's False

# For Non Boolean Data Types
#       0 means False
#       non-zero means True
#       empty string is always treated as False
#  E.g x and y
# if x is 0 and y is 10 ans will be ==> 0
# if x is 0 or y is 10 ans will be ==> 10
# if x is 0 not y is 10 ans will be ==> 0