"""
What is a variable?
A variable is nothing but a resevered memory location to store values or data.
Every variable must have some datatype.
It can be string, integer, triple, complex, dictionary, range datatypes
Python is dynamic type of programming language
Every Variable is associated a specific datatype
A dynamic programming language based on the variable the datatype of the variable is automatically accept
There are different ways of creating variable with the same values
There is a result memeroy location as seen in the example below
In Java you need to declare a variable and provide the datatype of the variable 
Once you declare the variable with a datatype you can store some value
"""

a = 10 # "a" is the memory location storing a value of "10" dtatype
# "a" is also the varaibale name storing some integer datatype
# The datatype is automatically assigned to variable "a"
b = 20.5 # b is a variable storing a floating value of datatype
c = 'welcome' # c is a variable storing a string datatype and double or single quote is a character declaring a string datatype
# Above are ways of declaring a variable and providing dataypes
a,b,c = 10,20.5,'welcome' # each variable is assigned a datatype
a=b=c = 100
print(a,type(a))
print(b,type(b))
print(c,type(c))

a = 100
print(a) # 100 is printed as output
a = "welcome"
print(a) # welcome is also printed as output

# Despite updating "a" with the variable with a different value, python always considered the last and latest statement
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
AFter using a variable, it is highly recommended to delete that variable if it's no longer required in order for the corresponding object is
eligible for Garbage Collection.
Unbind means ==> cannot be reversed. After deletion, trying to access the variable will throw a NameError because the variable is no longer exist.
Python has automatic memory management, and variables are typically cleaned up by the garbage collector when they are no longer referenced.
E.g
'''
a = 100
print(a)
del a
print(a) # NameError

'''
Output is
100
Traceback (most recent call last):
    print(a) # Name error
          ^
NameError: name 'a' is not defined

We can only delete variables which are pointing to immutable objects. 
But we cannot delete the elements present inside the immutable obejct.
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
print(s) # NameError

'''
Output is 
Traceback (most recent call last):
    print(s)
          ^
NameError: name 's' is not defined

Once it's deleted it can't be retraced again

String is an immutable datatype.
E.g from the above script "welcome", "w" in welcome is an important elelment likewise the other leters in "welcome" word.
And all these letters are available in the string datatype "welcome".
However, one cannot delete a letter from the string datatype or immutable object "welcome" e.g "w' or "l" or "m" can't be deleted from the word or object.
We can only access the "welcome" object by using indexing
E.g (below script is the continuation from the above script)
'''
print(s[0]) # output is "w"
print(s[1]) # output is "e"
print(s[5]) # output is "m"
'''
We can access the immutable individual object with index by specifying the location of the element so that it can be accessible.
Also, we cannot delete the individual element by using the "del" keyword and index despite specifying the location of the element to be deleted.
E.g writing the below script to delete an element from the "welcome" object will throw a TypeError
'''
del s [3]

'''
Output is
del s [3]
        ~~^^^
TypeError: 'str' object doesn't support item deletion

The above error message shows there's an element but can't be deleted because string is an immutable object
Once we understand the jagons or anatomy of variables, it's important to understand datatypes in python
'''