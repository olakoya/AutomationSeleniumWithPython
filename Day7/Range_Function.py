# Range Function
# ---------------
# For notes to support the below codes, check Day 3 ControlStatement Notes File
# Python file is a range of module, and we can create class, functions etc inside this module 
'''
Form - 1 ==> range(stop) starts from 0
Form - 2 ==> range(start,stop)
Form - 3 ==> range(start,stop, step) stops at -1
'''
# Form - 1 ==> range(stop) starts from 0
# ---------------------------------------
print(list(range(20))) # range(20)
# range is like a keyword that only generate a sequence of numbers and not for any other purpose
#----------------------------
# range will generate a sequence of numbers from 0
# we can convert it to a list of datatype by adding "print(list())"
'''
Output for print(list(range(20))) is
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Which gives us a sequence range of numbers by default from 0
'''
print(range(20))
'''
Output is 
range(0, 20)
This gives us a range of numbers
'''
print(list(range(200)))
'''
Output is 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 
89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 
115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 
139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 
163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 
187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]
The gives a sequence that started from 0 and ends in 199
'''

# From instance if we want to start the range from 75, this is where we use Form 2 range (start, stop)
# Form - 2 ==> range(start,stop)
# ------------------------------
print(list(range(75,200,1))) # the start value here is 75 and it stops at 200 with 1 step each to next number on the list
'''
Output is 
[75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 
105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 
130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 
155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 
180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]
'''

# Step Value 
# ------------
print(list(range(50,201,3))) # the step value here is 3 and it's positive i.e. 3 steps each to next number on the list
'''
Output is 
[50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 
137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173, 176, 179, 182, 185, 188, 191, 194, 197, 200]
'''

# To generate only odd numbers starting from 1 to 100, code to use is;
range(1,101,2)
# 1, 3, 5, 7, 9 ==> odd numbers
# lets add list data structure "print(list())" to the range

print(list(range(1,101,2))) # starting from 1 with consecutive number difference of 2
'''
Output is
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 
69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
'''
range(2,101,2)
# 0, 2, 4, 6, 8, 10 ==> even numbers
# lets add list data structure "print(list())" to the range
print(list(range(2,101,2))) # starting from 2 with consecutive number difference of 2
'''
Output is
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 
70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
''' 
print(list(range(2,101,4))) # starting from 2 with consecutive number difference of 4
'''
Output is 
[2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]
'''
print(list(range(0,101,4))) # starting from 0 with consecutive number difference of 4
'''
Output is
[0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100

Any number divisible by 2 or 4 is even number.
Division isn't a step value
'''

# Form - 3 ==> range(start,stop, step) step is negative
# ------------------------------------------------------
"""
Step value always decides the difference between 2 consecutive numbers
Default value of step is 1

Step ==> positive ==> forward direction ==> L to R ==> stop or end at + 1
Step ==> negative ==> reverse direction ==> R to L ==> stop or end at - 1

0, 2, 4, 6, 8, 10 ==> even numbers
1, 3, 5, 7, 9 ==> odd numbers
"""

range(10,1) # because we are moving in the step value direction we are going to start from -1
# 10 is the last value when we move in the forward direction and step value is 0
# 10 is the first value when we move in the reverse direction and the step value is -1
# stop value is 1 ie the number in the middle

range(10,1,-1)
print(list(range(10,1,-1)))
'''
Output is
[10, 9, 8, 7, 6, 5, 4, 3, 2]
'''
range(10,1,1)
print(list(range(10,1,1)))
'''
Output is 
[] ie blank
'''
range(-10,1,5)
print(list(range(-10,1,5)))
'''
Output is 
[-10, -5, 0]
'''
print(list(range(-10,5)))
'''
Output is 
[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
'''
print(list(range(-10,-5)))
'''
Output is 
[-10, -9, -8, -7, -6]
'''
# Different types of a range functions are: range(start,stop, step) stops at -1
# ------------------------------------------------------------------------------
print(list(range(10,1,-1))) 
# It will generate sequence of numbers starting from 10 and ends with 1 in a reverse direction and decrement of -1 step value
print(list(range(10,1,1))) 
# It will generate Empty set of numbers starting from 10 and ends with 1 in a forward direction and increment of +1 step value
print(list(range(10,15,-1))) 
# It will generate Empty set of numbers starting from 10 and ends with 15 in increment of -1 of which it isn't possible
print(list(range(15,10,1)))
# It will generate Empty set of numbers starting from 15 and ends with 10 in a forward direction and increment of +1 step value
'''
Output are
[10, 9, 8, 7, 6, 5, 4, 3, 2]
[]
[]
[]

This range of cunction can by use for 'for' loop
'''
