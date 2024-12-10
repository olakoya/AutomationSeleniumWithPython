'''
Accessing Characters inside String
-----------------------------------
s = "welcome" 
s = "Hello"

Types are:
----------
1. Index 
2. Slice operator

Every character inside string will have address or location or index.
With the help of address or location or index we can access data inside a string.
E.g
s = "welcome" (w e l c o m e ) in the string are all individual character that has an address or location


1. Accessing characters by index
------------------------------
Python support both +ve and -ve indexing
+ve and -ve characters are called index

0   1   2   3   4
H   E   L   L   O
-5  -4  -3  -2   -1

+ve ==> (L to R) ==> forward direction

-ve <== backward direction <== (R to L)

In the forward direction ==> the first index is "0" for the "H" character as seen from above

First character in forward direction has an index of 0
Last character index in forward direction is len-1 i.e. length - 1
Likewise:
First character in backward/reverse direction has an index of -1
Last character in backward/reverse direction direction is -len

Len means count of characters e.g
0   1   2   3   4   5   forward index
p   y   t   h   o   n
-6  -5  -4  -3  -2  -1  reverse index

Based on the above index value, one can get a character from the address and get a data inside the string.
'''

# print (s)
s = "welcome"
'''
0   1   2   3   4   5   6
w   e   l   c   o   m   e
-7  -6  -5  -4  -3  -2  -1
'''
# I want a data or character and specify single character
# To loacte the index in the above string code, code to use is 
s [3] # accessing the character by using the index value [3]
print(s[3])
'''
Output is 
c
'''
print(s[-6])
'''
Output is 
e
'''
print(s[20])
print(s[-20])
'''
Output for both are
IndexError: string index out of range

It throws indexerror because no range of index.

If we are trying to access character of a string without range of index then we will get Index Error
0 < x < len(str)-1
In Forward index value for welcome, equation will be 0 < x < 7-1 i.e 0<x<6
And because index value is[20] isn't in a range of 0 < 20 < 6 it outputs an "indexerror" result

In Reverse index value for welcome, equation will be -1 < -20 < -7 
And because index value is[20] and isn't in a range of -1 < 20 < -7 it outputs an "indexerror" result

Index value must always be picked from range of characters
String is very important to datatype
'''

# Writing a program to accept some strings from keybaord and display it's character in index wise

s = input("Enter some string = ") # input method to use and storing some strings inside a variable
# To access sequence inside a variable we use for loop
for x in s:
    print(x)
'''
Output is
Enter some string = Ola
O
l
a
'''
'''
0   1   2   3   4   5   6      forward index numbers
M   A   D   H   A   V   I
-7  -6  -5  -4  -3  -2  -1      reverse index numbers

I want to print in index characters and what to do is
i = 0 (as per 1st character from the forward index number)
len = 7 (0-7 = 7 i.e. total number of MADHAVI characters in the forward direction)
1-7 = -6 (i.e. total number of MADHAVI characters in the reverse direction)
'''
s = input("Enter some string = ")
i = 0
for x in s:
    print(i,i-len(s),x) # i.e. print(0,0-7(s),x)
    i = i+1 # 0+1
'''
0 -7 M
1 -6 A
2 -5 D
3 -4 H
4 -3 A
5 -2 V
6 -1 I
'''
'''
Output is 
Enter some string = JesusChrist
0 -11 J
1 -10 e
2 -9 s
3 -8 u
4 -7 s
5 -6 C
6 -5 h
7 -4 r
8 -3 i
9 -2 s
10 -1 t
'''
# Output needs to be in a clear readable format
s = input("Enter some string = ")
i = 0
for x in s:
    print(f"The character present at positive index {i} and at negative index {i-len(s)} is {x}") 
    i = i+1 
'''
Output is
Enter some string = Madhavi
The character present at positive index 0 and at negative index -7 is M
The character present at positive index 1 and at negative index -6 is a
The character present at positive index 2 and at negative index -5 is d
The character present at positive index 3 and at negative index -4 is h
The character present at positive index 4 and at negative index -3 is a
The character present at positive index 5 and at negative index -2 is v
The character present at positive index 6 and at negative index -1 is i

The above is formatting the output from the string format (f) above
And the logic used is {i}, {i-len(s)}, {x} in for loop
'''