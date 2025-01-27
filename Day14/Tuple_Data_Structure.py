'''
Tuple Data Structure
---------------------
Tuple is also like List Data Structure
Once we have a Tuple we cannot modify, increase or decrease the size
Tuple is Read only version of List

Tuple elements are separated by comma and enclosed in parenthesis (Optional but recommended)
E.g
'''

# Create a Tuple
# t1 = () # empty parenthesis ie bracket that is an empty tuple
# t2 = (10,2,34,5,"string",10+6j) # element in advance
# t3 = (10) # single valued tuple
# t4 = eval(input("Enter some data = "))
# t5 = tuple(range(10))
# t6 = tuple("Learning pyhton is easy".split())
#
# print(type(t1))
# print(type(t2))
# print(type(t3))
# print(type(t4))
# print(type(t5))
# print(type(t6))

'''
Output is
Enter some data = (1,2,3)
<class 'tuple'>
<class 'tuple'>
<class 'int'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>

2nd execution Output is
Enter some data = 1,2,3
<class 'tuple'>
<class 'tuple'>
<class 'int'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
'''

'''
Single Valued Tuple
--------------------
(20,) ==> Tuple

Access Elements of a Tuple
---------------------------
1. Index
2. Slice Operator
E.g
'''
# t = 1,2,'a','python',10+9j
# print(type(t))
# print(t)
'''
Output is
<class 'tuple'>
(1, 2, 'a', 'python', (10+9j))
'''
# print(t[6]) # index error
'''
print(t[6]) # index error
IndexError: tuple index out of range
'''
# print(t[3])
# print(t[-3])
# print(t[1:2:3])
# print(t[1:3:1])
# print(t[3:1:-1])
'''
Output is
python
a
(2,)
(2, 'a')
('python', 'a')
'''

# Traversing

# t = (1, 2, 'a', 'python', 10 + 9j)  # Tuple initialization
#
# # Using while loop
# i = 0  # Initialization
# while i < len(t):  # Loop condition to iterate through the tuple 0 1
#     print(t[i])  # Print the current element 10 20 30 40
#     i += 1  # Increment the index 1 2 3 4
#
# # Using for loop
# for eachele in t:
#     print(eachele)  # Print each element in the tuple
'''
Output is
1
2
a
python
(10+9j)
1
2
a
python
(10+9j)
'''

# Tuple vs Mutability
# t = 1, 2, 'a', 'python', 10 + 9j
# print(t)
# t[1] = 100
# print(t)
'''
Output is
line 115, in <module>
    t[1] = 100
TypeError: 'tuple' object does not support item assignment
'''

'''
A TUPLE IS READ ONLY VERSION OF LIST
'''

# Mathematical Operations ==> Concatenation and Repetition
# t1 = 10,20,30
# t2 = 'a', 'b', 'c'
# print(t1 + t2)
# print(t1*5)
'''
Output is
(10, 20, 30, 'a', 'b', 'c')
(10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30)
'''

# Functions on Tuple
# s = (10,20,30,40,50,20)
# print(len(s))
'''
Output is 
6
'''
# print(s.count(20))
# print(s.index(30))
# print(sorted(s))
'''
Output is
2
2
[10, 20, 20, 30, 40, 50]
'''

'''
Tuple Packing and Unpacking
----------------------------
- Tuple packing is the process of combining multiple values into a single tuple in a single statement.
- Tuple unpacking is the process of assigning the values from a tuple to multiple variables in a single statement.
- Tuple unpacking is the reverse process of Tuple packing.
Note: During tuple unpacking, the number of variables must watch match the number of values otherwise, a ValueError will occur.

E.g
'''
a = 10
b = 20

# t = a,b
# print(t)
'''
Output is
(10, 20)
'''
t = 10,20,30
a,b,c = t

print(a)
print(b)
print(c)
'''
10
20
30
'''