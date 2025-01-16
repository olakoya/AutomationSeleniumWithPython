'''
List Data Structure
--------------------
- This represents a group of individual objects as a single entity which is called ==> List
E.g x = 10 and 10 is variable and it's unable to install more variable in x
- In Insertion order is preserved
- List is Heterogeneous Type of data
_ List is Dynamic and mutable
- List is separated by comma enclosed in square brackets
E.g x = 10, 'a', 'python', 10+i10 the variables are separated with commas
    [x = 10, 'a', 'python', 10+i10] Putting them in square bracket make it a list
- List supports indexing
E.g
'''
from gc import is_finalized

# Creating a List
# x = [] # empty list i.e. unknown list
# y = [10,20,30] # elements in advance
# z = input("Enter Data = ") # treated as string data type
# w = eval(input("Enter Data = ")) # eval convert inputs to appropriate datatype
# a = list(range(11)) # range generates the sequence of numbers and using list to convert to data structure
# b = "Learning python is very easy".split() # split is based on some separations
#
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(w))
# print(type(a))
# print(type(b))
'''
Output is
Enter Data = 10
Enter Data = 10, 20
<class 'list'>
<class 'list'>
<class 'str'>
<class 'tuple'>
<class 'list'>
<class 'list'>
'''

# Access element in the list
# list = [10,20,30,40]
# print(list[1])
# print(list[-2])
'''
Output is
20
30
'''

# Slice operator

# print(list[2::2])
# print(list[2::1])
# print(list[2::-1])
'''
Output is
[30]
[30, 40]
[30, 20, 10]

----------------------------------
'''

'''
List vs Mutable
-----------------
Once we create a list we can modify it's content
E.g
'''
# Mutable
# list = [10,20,30, 40]
# print(list)
# list[1 ]= 200
# print((list))
# '''
# Output is
# [10, 20, 30, 40]
# [10, 200, 30, 40]
#
# --------------------------------------
# '''
#
# '''
# Traversing
# -----------
# Sequential access of elements inside a list
#     while loop
#     for loop
# E.g
# '''
# list = [10,20,30,40] # 0 1
# i = 0 # initialisation # 10 20 30 40
# while i<len(list):
#     print(list[i])
#
#     i = i+1 # 1 2 3 4
# '''
# Output is
# 10
# 20
# 30
# 40
# '''
# # for loop
# for eachele in list:
#     print(eachele)
# '''
# Output is
# 10
# 20
# 30
# 40
# '''
#
# # Functions on list data structure
# a = [10,20,30,40,50,60,70,80,90]
# print(len(a))
# '''
# Output is
# 9
# '''
# a = [10,20,30,40,50,60,70,80,90,50,30,60,10,50,20,20]
# print(a.count(20))
# print(a.index(40))
# (a.append(90))
# print(a)
# '''
# Output is
# 3
# 3
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 50, 30, 60, 10, 50, 20, 20, 90]
# ---------------------------------------------------------
# '''
#
# '''
# Append function always adds element in last position i.e. at the end of the list
# Insert function is ==> adds element at specified index position
#
# E.g
# '''
#
# a.insert(2, 100)
# print(a)
# '''
# Output is
# [10, 20, 100, 30, 40, 50, 60, 70, 80, 90, 50, 30, 60, 10, 50, 20, 20, 90]
# '''
#
# a.extend([200, 300])
# print(a)
# '''
# Output is
# [10, 20, 100, 30, 40, 50, 60, 70, 80, 90, 50, 30, 60, 10, 50, 20, 20, 90, 200, 300]
# '''
#
# a.remove(50)
# print(a)
# '''
# Output is
# [10, 20, 100, 30, 40, 60, 70, 80, 90, 50, 30, 60, 10, 50, 20, 20, 90, 200, 300]
#
# remove ==> removes a specific elements
# pop  ==> removes random elements if we don't specify index position
# E.g
# '''
# print(a.pop())
# print(a)
# '''
# Output is
# 300
# [10, 20, 100, 30, 40, 60, 70, 80, 90, 50, 30, 60, 10, 50, 20, 20, 90, 200]
# '''
#
# '''
# Default Natural Sorting Order
# ------------------------------
# Integers ==> Ascending Order
# Alphabets ==> Alphabetical Order
# E.g
# '''
# a.sort()
# print(a)
# '''
# Output is
# [10, 20, 100, 30, 40, 60, 70, 80, 90, 50, 30, 60, 10, 50, 20, 20, 90, 200]
# [10, 10, 20, 20, 20, 30, 30, 40, 50, 50, 60, 60, 70, 80, 90, 90, 100, 200]
# '''
#
# a.clear()
# print(a)
# '''
# Output is
# []
# '''

'''
Aliasing of List Objects
---------------------------
- The process of giving another reference variable to the existing list is called aliasing.
- The problem in this approach is by using one reference variable if we are changing content, then those changes will be 
    reflected to the other reference variable.
E.g y = [10,20,30,40]
    x = y
E.g
'''
# Aliasing
# y = [10, 20, 30, 40]
# x = y
# print(y)
# print(x)
# y[3] = 100
# print(y)
# print(x)
'''
Output is
[10, 20, 30, 40]
[10, 20, 30, 40]
[10, 20, 30, 100]
[10, 20, 30, 100]
'''
# y = [10, 20, 30, 40]
# x = y
# print("y:", y)
# print("x:", x)
# y[3] = 100
# print("After modifying y:")
# print("y:", y)
# print("x:", x)
'''
Output is
y: [10, 20, 30, 40]
x: [10, 20, 30, 40]
After modifying y:
y: [10, 20, 30, 100]
x: [10, 20, 30, 100]
'''

'''
Cloning of List Objects
-------------------------
The process of creating exactly duplicate independent object is called cloning.
We can implement cloning by using slice operator or by using copy() function
E.g
'''
# # Cloning --- Slicing
# y = [10, 20, 30, 40]
# x = y[::]
# print(y)
# print(x)
# y[3] = 100
# print(y)
# print(x)
'''
Output is
[10, 20, 30, 40]
[10, 20, 30, 40]
[10, 20, 30, 100]
[10, 20, 30, 40]
'''
# y = [10, 20, 30, 40]
# x = y[::]  # cloning using slicing
# print("y:", y)
# print("x:", x)
# y[3] = 100
# print("y:", y)
# print("x:", x)
'''
Output is
y: [10, 20, 30, 40]
x: [10, 20, 30, 40]
y: [10, 20, 30, 100]
x: [10, 20, 30, 40]
'''

# Cloning --- Copying
# y = [10, 20, 30, 40]
# x = y.copy()
# print(y)
# print(x)
# y[3] = 100
# print(y)
# print(x)
'''
Output is
[10, 20, 30, 40]
[10, 20, 30, 40]
[10, 20, 30, 100]
[10, 20, 30, 40]
'''

# Operators on List
# Concatenation and Repetition
# a = [1,2,3]
# b = [4,5,6]
#
# print(a+b)
# print(a*4)
# print(b*3)
'''
Output is
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
[4, 5, 6, 4, 5, 6, 4, 5, 6]
'''

# Membership Operators
a = [1,2,3]
print('c' in a)
print('c' is not a)
'''
Output is
False
True
'''

'''
List Comprehension
-------------------
Easy and compact way if creating a list data structure from another sequence like list, tuple, dictionary, set, string.

Syntax
-------
    [expression for ele in sequence if condition]
E.g
'''
y = [x*x for x in range(1,11) if x%2] # for loop sequence-range(1,11) and expression-x*x
print(y)
'''
Output is
[1, 9, 25, 49, 81]
'''

y = [x*x for x in range(1,11) if x%2==0] # for loop sequence-range(1,11) and expression-x*x
print(y)
'''
Output is
[4, 16, 36, 64, 100]
'''