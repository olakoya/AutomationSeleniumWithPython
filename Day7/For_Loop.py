'''
FOR LOOP FUNCTION 
------------------
If we want to execute some action for every element present in some sequence i.e. string or collection (dictionary) then we should go for loop.
Body will be executed for every element present in the sequence.
Sequence means a group of string or collection (tuple, dictionary etc are collections) then we should go for loop.
Body will be executed for every element present in the sequence.
Range function is called a collection and it's used along with for loop.
Any sequence is also called a range of collection.
Example of sequence of collection is [10, 9, 8, 7, 6, 5, 4, 3, 2]

Syntax of For Loop
-------------------
For every element in sequence an action is performed
Perform an action e.g Body (in a body we have a statement)
Action we can specify on body
'''
# print numbers from 1 to 10
# ---------------------------
for x in range(1,11):
# 'for' every element in the "range(1,11)" sequence 
    print(x)
# perform an action "print(x)"
'''
Output
1
2
3
4
5
6
7
8
9
10
'''
# To change it the range from list to one line code to use is
for y in range(1,11):
    print(y,end=" ")
'''
Output is 
1 2 3 4 5 6 7 8 9 10 
'''

# print numbers from 10 to 1 (i.e. we need to follow (start,stop, step) sequence)
# ---------------------------
for x in range(10,0,-1): # after condition we need to always specify colon :
    print(x)
'''
Output is 
9
8
7
6
5
4
3
2
1
'''

# print even numbers (usung: start,stop, step)
# --------------------------------------------
# range of functions will genereate the even numbers
for x in range(0,21,2):
    print(x)
'''
Output is 
0
2
4
6
8
10
12
14
16
18
20
'''
# print odd numbers (usung: start,stop, step)
# --------------------------------------------
for x in range(1,21,2):
    print(x)
'''
Output is
1
3
5
7
9
11
13
15
17
19
'''