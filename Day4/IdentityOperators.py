# Identity Operators 
# It addresses comparison
# This means if two objects are pointing to two different things ie two variables pointing to the same object is Identity
#   is ==> True, False (It will return True if both obejects are the same and False if not the same)
#   is not ==> True, False (It will return False if both objects are the same and True if not the same)
# E.g. 
x = 10
y = 10
# The above example means that both x and y are pointing to the same object called "10" i.e same address

# In python everything is treated as an object

a = 20
b = 30
# This means both variables are pointing different objects as they are having different ids
# To verify the address we will use identity operators

x = 10
y = 10

print(id(x))
print(id(y))

print(x is y)
print(x is not y)
'''
Output for both variables is True for "is" and False for "is not" for pointing to the same objects
4530416672
4530416672
True
False
'''

a = 20
b = 30

print(id(a))
print(id(b))

print(a is b)
print(a is not b)
'''
Output for both variables is False for "is" and True for "is not" for pointing to different objects
4530416992
4530417312
False
True
'''

# Above is how to check the presence of an element in a sequence value or compare the presence by an identity operator