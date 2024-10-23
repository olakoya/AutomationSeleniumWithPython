# Ternary Operators returns sysntax values
# syntax
#   x = firstValue is condition else secondValue

# if condition:
#   return firstValue
# else:
#   return secondValue

# If condition is True then firstValue will be considered else secondValue will be considered.
# E.g

# input("Enter First number = ")

# Reading Dynamic Input from the Keyboard
# In Python we have input() method and every input value is treated as str (string) type only

# a = input("Enter First number = ")
# # print(type (a)) # <class 'str'> string data type
# b = input("Enter second number = ")
# print(a+b) 

# + between strings is treated as an concatenation (joinng) operator.
# E.g. 
# "Hello" 
# "Bharhati"
# "Hello"  + "Bharhati" ==> "HelloBharhati"
# "10" + "20" ==> 1020
# The above are strings but when you convert them to addition it's called interger Called Type Casting

# Type Casting
# It means conevrting from one datatype to another datatype e.g string to boolean value or integer to boolean value
# E.g
a = int(input("Enter First number = "))
b = int(input("Enter second number = "))
print(a+b) 

# To check minimum and maximum numbers what to do is 
# syntax ==> x = firstValue is condition else secondValue
# E.g
x = a if a<b else b
print("minimum value is ", x)
y = a if a>b else b
print("maximum value is ", y)