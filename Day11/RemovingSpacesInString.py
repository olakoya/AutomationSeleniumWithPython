'''
Removing Spaces from the String
---------------------------------
There are 3 different functions to remove spaces from String datatype
1. rstrip: This will remove spaces at the right hand side of the string
2. lstrip: This will remove spaces at the left hand side of the string
3. strip: This will remove spaces from both left and right sides of the string

String is immutable datatype i.e any changes made is a new string(new object created) which is storing another variable
E.g:
'''
name = " John Cena "
sname = name.rstrip()
name.rstrip()
sname = name.lstrip()
sname = name.strip()
print(name)
print(sname)
'''
Output is
 John Cena 
 
 Output after adding line 13
 John Cena 
  John Cena
 
 Output after adding line 15
 John Cena 
John Cena 

Output after adding line 16
 John Cena 
John Cena
'''

'''
Comparision of Strings
------------------------
10 20 
lexicographyically
ASCII CODE: This is the comparison of two strings

ord() ==> returns ascii code
chr() ==> return character based on ascii code..

s1 = 'shyla'
s2 = "Ravindra'
E.g
'''
s1 = "john"
s2 = "cena"

print(s1<s2) # False
print(s1>s2) # True
print(s1<=s2) # False
print(s1>=s2) # True

print(s1==s2) # False
print(s1!=s2) # True
'''
Output is
False
True
False
True
False
False
'''
# E.g 2
print(ord('j')) # 106
print(ord('c')) # 99
'''
Output is 
106
99
'''
'''
Finding SubStrings
-------------------
4 Functions are;
i. find() ==> returns index of a substring where it has first occurred
                When substring isn't available it returns -1
ii. index() ==> returns index of a substring where it has first occurred
                When substring isn't available it returns ValueError
iii. rfind() ==> returns index of a substring where it has last occurred
                When substring isn't available it returns -1
iv. rindex() ==> returns index of a substring where it has last occurred
                When substring isn't available it returns ValueError
E.g
'''
s = "abababababababaabbabbaab"
sub = 'a'
sub = 'c'

print(s.find(sub)) # Output is 0
print(s.index(sub)) # Output is 0

print(s.rfind(sub)) # Output is 22
print(s.rindex(sub)) # Output is 22
'''
Output after adding line 93 to execute lines 95 & 98 is 
-1
-1

Output after executing for line 96 and line 99 is
line 96, in <module>
    print(s.index(sub)) # Output is 0
ValueError: substring not found

To check if index substring function is available one needs to use membership operators
'''

'''
Displaying Positions of SubString in a MainString
---------------------------------------------------
i. find(sub,begin,end) this is how the function is executed
E.g
'''
s = "abababababababaabbabbaab"
sub = 'a'

flag = False
pos = -1

while True:
    pos = s.find(sub,pos+1,len(s)) # Output is 0 automatically
    if pos == -1:
        break
    print("Found at position",pos)
    flag = True

if not flag:
    print("Not found")

'''
Output is 
Found at position 0
Found at position 2
Found at position 4
Found at position 6
Found at position 8
Found at position 10
Found at position 12
Found at position 14
Found at position 15
Found at position 18
Found at position 21
Found at position 22
'''
