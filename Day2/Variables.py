"""
What is a variable?
A variable is nothing but a resevered memory location to store values or data.
Every variable must have some datatype.
It can string, integer, triple, complex, dictionary, range datatypes
Python is dynamic type of programming language
Every Variable associated to explicity specific to a datatype
A dynamic programming language based on the variable the datatype of the variable is automatically accept
Different ways of creating variable with the same values
There is a result memeroy location as seen in the example below
In Java you need to declare a variable and provide the datatype of the variable 
Once you declare the variable with a datatype you can store some value
"""

a = 10 # "a" is the memory location storing a value "10"
# "a" is the vraibale name storing some integer data
# The datatype is a automatically assigned to variable "a"
b = 20.5 # b is a variable storing a floating value of datatype
c = 'welcome' # c is a variable storing a string datatype and double of single quote is a character declaring a string datatype
# Above are ways of declaring a varaible and providing dataypes
a,b,c = 10,20.5,'welcome' # each variable is assigned a datatype
a=b=c = 100
print(a,type(a))
print(b,type(b))
print(c,type(c))

a = 100
print(a) # 100 is printed as output
a = "welcome"
print(a) # welcome is also printed as output

# Despite updating "a" the variable with a different value, python always considered the last and latest statement
# This is respect to variables

'''
Output of the above is
10 <class 'int'>
20.5 <class 'float'>
welcome <class 'str'>

100 <class 'int'>
100 <class 'int'>
100 <class 'int'>

100
welcome

Remember that a variable is a container in a memory location to store data as values
Based on the value provided during run time the datatype of the variable is automatically assigned by python intepreter
This type of behaviour is a dynamic behaviour, therefore python is a dynamically type of programming language not syntactically one
Syntactically is a type of programing lanaguage you will need to provide it's datatype before execution
'''
'''
Understanding how a variable can be deleted:
It can be done by using "del keyword", Del is a keyword in Python.
Among the 35 keywords list "del" is included and part of the keywords. Del should never be use except for deleting purposes.
AFter using a variable, it is highly recommened to delete that variable if it's no longer required in order for the corresponding object is
eligible for Garbage Collection.
Unbind means ==> cannot be reversed. After deletion, trying to access the variable will throw a NameError because the variable no longer exist.
Python has automatic memory management, and variables are typically cleaned up by the garbage collector when they are no longer referenced.
E.g
'''
# a = 100
# print(a)
# del a
# print(a) # NameError

'''
Output is
100
Traceback (most recent call last):
  File "/Users/olakoya/Desktop/automationwithpython/Day2/Variables.py", line 67, in <module>
    print(a) # Name error
          ^
NameError: name 'a' is not defined

We can delete variables which are pointing to immutable objects. But we cannot delete the elements present inside immutable obejct.
E.g
'''
s = "welcome" # s is an immutable object string and because of that the object can be deleted. 
# "welcome" is an insequence charater pointing to the object which can be deleted
print(type(s))

'''
Output is 
<class 'str'>

And with the below script if we try to execute it again it will give us NameError
'''
del s
print(s)

'''
Output is 
Traceback (most recent call last):
  File "/Users/olakoya/Desktop/automationwithpython/Day2/Variables.py", line 91, in <module>
    print(s)
          ^
NameError: name 's' is not defined

Once it's deleted it can't be retraced again
'''