# Counting Substring
s = "Donald Trump Donald"
sub = 'Donald'

print(s.count(sub)) # function without beginning and ending
'''
Output is 
2
'''

'''
Replacing a string with another string
---------------------------------------
Replace (oldsrting, newstring i.e passing as a parameter)

E.g
'''
s = "Learning python is very difficult"
s1 = s.replace("difficult", "easy") # string is an immutable data type
print(s)
print(s1)
'''
Output is
Learning python is very easy

Output after adding line 20
Learning python is very difficult
Learning python is very easy
'''
'''
Once we creates string object, we cannot change the content.
This is non changeable behaviour is nothing but immutability.
If we are trying yo change the content by using any method, then with those changes a new object will be created and changes 
won't happened in existing object.
Hence with replace() method also, a new object that will be created but existing object won't be changed 
Example is on the line of codes above in 18 to 21

Mutable means can change
Immutable means unchanged e.g string

----------------------------------------------------
'''

'''
Split the strings
----------------
s.split(separator)

s = "05/November/2024" this is a string immutable
To split the date above, what to do is add the below code line
s.split("/")
s.split("-")

By default separator is a space and vice versa 
After splitting it will return List of Data Structure
E.g
'''

# Splitting the string
s = "Learning python is very very interesting"
print(s.split())
'''
Output is 
['Learning', 'python', 'is', 'very', 'very', 'interesting']
'''
# E.g 2
s = "22-10-2024"
print(s.split("-"))
'''
Output is
['22', '10', '2024']
'''
# E.g 3
s = "22-$10-2024"
print(s.split("-"))
'''
Output is
['22', '$10', '2024']

--------------------------------
'''

'''
Join the Strings
------------------
join(sequence)

Sequence can be a ==> range, string, list, tuple, set, dictionary data structure 

join(strings) based on some separator it can be joined
Strings means group of strings
separator.join(group of strings)

E.g
'''
# Join the Strings
print(list(range(10)))
'''
Output is
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

print(str(list(range(10))))
'''
Output is
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

print(type(str(list(range(10)))))
'''
Output is
<class 'str'>
'''

print(("-".join(s)))
'''
Output is
2-2---$-1-0---2-0-2-4
'''

s = {"Donald Trump", "Kamala Harris", "Vivek Ramaswany", "Barack Obama"} # calibraces
print(("-".join(s)))
'''
Output is
Vivek Ramaswany-Donald Trump-Kamala Harris-Barack Obama
'''

s = ["Donald Trump", "Kamala Harris", "Vivek Ramaswany", "Barack Obama"] # square brackets
print(("-".join(s)))
'''
Output is
Donald Trump-Kamala Harris-Vivek Ramaswany-Barack Obama
'''

s = ["Donald Trump", "Kamala Harris", "Vivek Ramaswany", "Barack Obama"] # square brackets
print(("/".join(s))) # using slash
'''
Output is
Donald Trump/Kamala Harris/Vivek Ramaswany/Barack Obama

------------------------------------------------------------
'''

'''
Change the case of the strings
-------------------------------
Upper() ==> To convert all characters to upper case
Lower() ==> To convert all characters to lower case
Swapcase() ==> To convert all lower case characters to upper case and vice versa
Title() ==> To convert all characters to title case i.e. first character in every word should be upper case and all 
            remaining characters should be in lower case
Capitalise() ==> Only first character will be converted to upper case and all remaining characters can be
                converted to lower case
E.g
'''
# Changing case of the strings
s = "Learning python is very very interesting"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
'''
Output is
LEARNING PYTHON IS VERY VERY INTERESTING
learning python is very very interesting
lEARNING PYTHON IS VERY VERY INTERESTING
Learning Python Is Very Very Interesting
Learning python is very very interesting

---------------------------------------------------
'''

'''
Checking presence of Substring at the beginning and ending of a string
------------------------------------------------------------------------
startswith(substring)
endswith(substring)
E.g
'''
s = "abcdefgh"
sub = "a"

print(s.startswith(sub))
print(s.endswith(sub))
'''
Output is
True
False

----------------------------------
'''

'''
Checking type of characters present in the string
----------------------------------------------------
isalnum() ==> Returns True if all characters are alphanumeric (a to z, A to Z, 0 to 9)
isalpha() ==> Returns True if all characters are alphabet symbols (a to z, A to Z)
isdigit() ==> Returns True if all characters are digits only (0 to 9)
islower() ==> Returns True if all characters are lower case alphabet symbols (a to z)
isupper() ==> Returns True if all characters are upper case alphabet symbols (A to Z)
istitle() ==> Returns True if string is in title case
isspace() ==> Returns True if string contains only spaces
E.g
'''
s = "abcd123"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.isspace())
'''
Output is
True
False
False
True
False
False
False
-----------------------------------
'''

'''
Formatting Output
-------------------
name = "Nandini"
name = "Shyla"
salary = "$25k"
salary = "25kinr"
country = "US"
country = "India"
E.g
'''
name = "Ola"
salary = "70000"
age = "47"

print(f"{name} 's salary is {salary} and his age ia {age} ") # f strings is used to format output without information
'''
Output is 
Ola 's salary is 70000 and his age ia 47 
'''
# E.g 2
print("{}'s salary is {} and his age ia {}" .format(name, salary, age))
'''
Output is 
Ola's salary is 70000 and his age ia 47
'''
# E.g 3
print("{}'s salary is {} and his age ia {}" .format(salary, age, name))
'''
Output is
70000's salary is 47 and his age ia Ola
Not meaningful


Method one in line 241 is best option code to use for f string method for spring formatting or spring data structure
'''
