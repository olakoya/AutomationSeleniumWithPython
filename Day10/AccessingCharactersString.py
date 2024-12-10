'''
Accessing Characters with Slice Operator
-----------------------------------------
Slice Operator means accessing ==> [range of indexes]
Every character has an address and the address has a locator and with the help of slice operator we will have a range of indexes

Syntax for Slice Operator
---------------------------
In a substring there are a range of datas and they are arranged as below;

string[beginindex:endindex:step]

beginindex is ==> from where we have to start slice (a piece)
endindex is ==> where we have to terminate our slice

Step values means the intervals between indexes (i.e. elements to skip between consecutive characters)
-------------------------------------------
+ve ==> moving from L to R ==> forward direction ==> endindex-1
-ve ==> moving from R to L ==> Reverse direction ==> endindex+1

Slice is ==> piece of substring (i.e. having a slice of a whole cake)
E.g
'''
s = "Learning python is very very easy"

print(s[1:7:1]) # [1stindex:slice operator:steps](i.e.[startindex:endindex:stopindex]) this substring is moving from left to right
'''
Output is 
earnin (i.e counting the letters which starting from 0 however, from the code its started from 1 until it gets to the 6th letter)
'''
print(s[1:7]) # this isn't specifying stepvalue unlike the above line 26 code that does 
'''
Output is 
earnin
'''
print(s[1:7:2]) # this is specifying steps value as 2 i.e skipping 2 steps forward
'''
Output is 
eri
'''
print(s[1:7:3]) # this is specifying steps value as 3 i.e skipping 3 steps forward and it can be either +ve or -ve
'''
Output is 
en
'''

'''
By default step value is 1
If we don't specify begin index by default slice operator will consider beginning of the string as 0
E.g
'''
print(s[:7]) # because the step value isn't given the execution will start from step 0 automatically till step :7
'''
Output is 
Learnin

If we don't specify end index by default slice operator will consider end of the string
E.g
'''
print(s[7:]) # because the step value isn't given the execution will start from step 7: automatically till the end
'''
Output is
g python is very very easy
'''
print(s[::]) # No starting index, beginnging index and step value
'''
Output is 
Learning python is very very easy
'''
print(s) # accessing string variable i.e. using a plain string without specfying stepvalue
'''
Output is 
Learning python is very very easy

If we don't specify beginning and ending indexes, by default slice operators will consider total string
'''
print(s[:]) # not specifying the beginning and ending index so output will give a total string by default
'''
Output is 
Learning python is very very easy
'''
print(s[::1]) # despite step given as 1 the output still given a total string
'''
Output is 
Learning python is very very easy
'''
print(s[0:10000]) # 0 to 29 is the range of indexes for the stringvalue 
'''
Output is 
Learning python is very very easy

If we specify index which is not in the range, by default slice operator will never raise index error as seen in the output above
'''
print(s[::-1]) # moving in the reverse direction via using -ve step of -1
'''
Output is
ysae yrev yrev si nohtyp gninraeL
'''
print(s[3:7:-1])
'''
Output is
empty string i.e. no output
'''
print(s[5:0:1])
'''
Output is
empty string i.e. no output
'''
print(s[9:0:0]) # step value can't never be 0, it has to always start from 1
'''
Output is 
ValueError: slice step cannot be zero
'''
print(s[0:-9:-2])
'''
Output is 
empty string
'''
s = "ola"
print(s[::-1])
'''
Output is 
alo
'''
s = input("Enter some string = ")
for x in s[::-1]:
    print(x)
'''
Enter some string = Ola
a
l
O
'''
s = input("Enter some string = ")
i = -1
for x in s[::-1]:
    print(i,x)
    i = i-1
'''
Enter some string = Ola
-1 a
-2 l
-3 O
'''
s = input("Enter some string = ")
i = -1
for x in s[::-1]:
    print(i,len(s)+i,x)
    i = i-1
'''
Enter some string = Ola
-1 2 a
-2 1 l
-3 0 O
'''