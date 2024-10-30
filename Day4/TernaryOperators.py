# Ternary Operators returns sysntax values i.e.
# What it does is that based on condition it returns value
# syntax
#   x is a value
#   x = if firstValue is condition else return secondValue
#   i.e. if condition is True else return False

# if condition:
#   return firstValue
# else:
#   return secondValue

# If condition is True then firstValue will be considered else secondValue will be considered.
# E.g

# input("Enter First number = ")

# Reading Dynamic Input from the Keyboard
# In Python we have input() method and every input value is treated as str (string) type only e.g.

a = input("Enter First number = ") # Output prompted user to enter a first number
print(type (a)) # Output is <class 'str'> string is the datatype
b = input("Enter second number = ") # Output prompted user to enter a second number
print(a+b) # "+"" between strings is known as Concatenation which means (joining) operator
# Output for above script will give the combination of a and b and not total number from the first and second numbers entered when prompted
# Because it's string so, if I enter 10 as 1st nos and 30 as 2nd nos the output of a+b will be 1030

# + between strings is treated as an concatenation (joinng) operator.
# E.g. 
# "Hello" 
# "Bharhati"
# "Hello"  + "Bharhati" ==> "HelloBharhati"
# "10" + "20" ==> 1020 (This is a strig datatype)
# The above are strings but when you convert them to addition it's called interger Called Type Casting

# Type Casting
# It means converting from one datatype to another datatype e.g string to boolean value or integer to boolean value
# E.g
a = int(input("Enter First number = ")) # Output prompted user to enter a first number
b = int(input("Enter second number = ")) # Output prompted user to enter a second number
print(a+b) # Output is total number after adding the 1st and 2nd nos entered when prompted

# To check minimum and maximum numbers what to do is 
# syntax ==> x = firstValue is condition else secondValue
# E.g
x = a if a<b else b
print("minimum value is ", x) 
y = a if a>b else b
print("maximum value is ", y) 
'''
Output for the above script
Enter First number = 90
Enter second number = 30
120
minimum value is  30
maximum value is  90
'''