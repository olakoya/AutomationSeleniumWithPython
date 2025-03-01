'''
Set Data Structure
-------------------
If we want to represent a group of unique (no duplicates) values as a single entity then we should go for set data structure.
Duplicates are not allowed.
Insertion order is not preserved, but we can sort the elements (set to a list, sort the list using sorted ()).
Indexing ans slicing not allowed for the set.
Heterogenous elements are allowed.
Set objects are mutable i.e. one we creates set object we can perform any changes in that object based on our requirement.
We can represent set elements within curly braces and with comma separation.
We can apply mathematical operations like union, intersection, difference etc on set objects.

E.g
'''
from pickletools import string1

# Creation of Set
# s = {}
#
# print(s)
# print(type(s))
'''
Output is 
{}
<class 'dict'>
'''

# s = () # empty set
# print(s)
# print(type(s))
'''
Output is 
()
<class 'tuple'>
'''

# s2 = {1,2,3,4,5,5}
# print(s2)
'''
Output is
{1, 2, 3, 4, 5}
'''

# s1 = ()
# s2 = {1,2,3,4,5,5}
# s3 = eval(input("Enter some data = "))
# s4 = set(range(10))
# s5 = set("Learning Python is very easy" . split())
# print(type(s1))
# print(type(s2))
# print(type(s3))
# print(type(s4))
# print(type(s5))

'''
Output is 
Enter some data = {1,2,3}
<class 'tuple'>
<class 'set'>
<class 'set'>
<class 'set'>
<class 'set'>
'''

# How to access Elements of the Set: Use For Loop and Why functions
# s = {1,2,3,4,5,5}
# for x in s:
#     print(x)

'''
Output is
1
2
3
4
5
'''
# s = {1,2,3,4,5,5}
# print(s[2])
'''
Output is
print(s[2])
TypeError: 'set' object is not subscriptable
'''

# Functions on Set Data Structure
# s = {10,20,30}
# print(s)
# s.add(40) # adding this to the above set
# print(s)
'''
Output is
{10, 20, 30}
{40, 10, 20, 30}
'''

# Adding Sequence to the above Data Set
# l = ['John', 'Trump', 'Obama']
# s.update(l)
# print(s)
'''
Output is 
{'John', 'Obama', 40, 10, 'Trump', 20, 30}
'''

# Cloning
# s1 = s.copy()
# print(s)
# print(s1)
'''
Output is
{'Obama', 40, 10, 20, 'Trump', 'John', 30}
{'Obama', 20, 'Trump', 40, 10, 'John', 30}
'''

# s = {10,20,30}
# s1 = s.copy()
# print(s)
# print(s1)
'''
Output is
{10, 20, 30}
{10, 20, 30}
'''
# print(s.pop())
'''
Output is
10
'''
# print(s)
'''
Output is
{20, 30}
'''
# s.remove(30)
# print(s)
'''
Output is
{20}
'''
# s.discard(20)
# print(s)
'''
Output is an empty set
set()
'''
# s.remove(20) # error
# print(s)
'''
Output is
  s.remove(20)
KeyError: 20
'''

'''
Mathematical Operations on Set

Types are:
---------
1. Union
2. Intersection
3. Difference
4. Symmetric Difference

To apply this set one needs to have 2 different data set e.g
'''
# x = {10, 20, 30, 40}
# y = {50, 60, 70, 20}
# print(x.union(y)) # combination of both elements
# print(x.intersection(y)) # common elements
# print(x.difference(y)) # elements in x and not in y
# print(x.symmetric_difference(y)) # not in x and not in y i.e. not in both

'''
Output is
{70, 40, 10, 50, 20, 60, 30}
{20}
{40, 10, 30}
{70, 40, 10, 50, 60, 30}
'''

# Check presence of Elements: This is possible by using membership
# x = {10, 20, 30, 40}
# print(60 in x)
# print(60 not in x)
'''
Output is
False
True
'''

'''
Set comprehension is supported in python

syntax
-------
[expression for ele in sequence if condition]
{expression for ele in sequence if condition}
E.g
'''
s = {x*x for x in range(11) if x%2 ==0}
print(s)
'''
Output is
{0, 64, 4, 36, 100, 16}
'''