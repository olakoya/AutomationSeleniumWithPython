'''
File Handling Session 2
------------------------
To perform any operation one needs to specify:
1. Open(filename, mode)
2. Actions
3. Close()

An operation must always close the file at the end of each operation and without which, it will be impossible to save and
might encounter many issues.

One can use both open and close method without which it's impossible to execute the operation

Developer will Open the file, QA Tester will perform Actions and also Close it

Specific method implemented are

Creating Python File with Statement
-------------------------------------
No Explicit close() method is required (i.e. this will take care of closing the file after going through operation)
The sudo code is;

i. Opening a file => open()
ii. Write Operation
iii. Read Operation
1v. Append Operation
v. With statement there's no need to close () as the statement will take care of it
E.g
'''
# with statement
# with the help of 'f' variable = open variable one would be able to perform this operation ("abc.txt", "w") as seen below
f = open("abc.txt", "w")
# to specify with "with" statement one needs to use 'with' at the beginning of the operation
with open("abc.txt", "w") as f: # this is alias 'as' i.e. given a name for open("abc.txt", "w") as 'f' (file)
# with, open, as are keywords used to handle this file
    f.write("File\n") # \ is a new line
    f.write("Handling\n")
    f.write("Session\n")
    print(f.closed) # this line doesn't guarantee close
# There's withblock from line 36 to 39 ie the space behind the 'f.'

print(f.closed) # but this does close the execution unlike line 39

'''
Output is
False
True

The 'true' output displayed that the file execution is closed
'''

# not issuing any close generally it might write some exceptions or issues or exceptions
# Lines 36 to 38 will specify the closure and to close line 39 will be used
'''
Without close() method below might happened
--------------------------------------------
Exceptions is that file will not properly close
There maybe chance of missing some data while
Close () must be specified all the time

Even if the .txt file isn't created one will be created during the time of execution
'''
'''
How to check if a file exist? One needs to import operating system, and from OS import a model
E.g
'''
# Approach 1
import os
print(os.path.isfile("abcd.txt")) # 'isfile' is a function - to check if file is available it will return Boolean value
# os model consists of a specific function 'isfile'
# During read 'r' operation it's important to know that the file exist otherwise it won't execute
'''
Output is 
False

Returns 'False' because the abcd.txt file isn't available and next is to 'if' statement below
'''
if os.path.isfile("abcd.txt"):
    with open("abcd.txt", "r") as f:
        print(f.readlines())
else:
    print("File isn't available")
'''
Output is
File isn't available
'''

# E.g of if a file is available
if os.path.isfile("abc.tx"):
    with open("abc.txt", "r") as f:
        print(f.readlines())
else:
    print("File is available")
'''
Output is
File is available
'''

# E.g Reading a content from an existing file
try:
    with open("abcd.txt","r") as f:
        print(f.readlines())
# Whatever code causes an exception is called risk assessing code so some lines are added to the above codes
except:
    print("Exception occurred because of File not found")

'''
Output is
Exception occurred because of File not found

If the data is present it will read content from it
'''

# Approach 2
from os.path import isfile
if isfile("abcd.txt"):
    with open("abc.txt", "r") as f:
        print(f.readlines())
else:
    print("File isn't available")
'''
Output is
['File\n', 'Handling\n', 'Session\n']

By changing code line 116 from 'abc.txt' to 'abcd.txt' to verify output if a file doesn't exist
Output is
File isn't available
'''

# Simple Operation on How to Access a Binary Data

# f1 = open(r"C:/Users/olakoya/Desktop/download.jpeg","rb")
f1 = open("/Users/olakoya/Desktop/download.jpeg", "rb")
f2 = open("newpic.jpg", "wb") # binary file is newpic.jpeg

bytes = f1.read()
print(bytes)
f2.write(bytes)

f1.close()
f2.close()
'''
Output is that 'newpic.jpg' file created inside the Day37 directory

And output after adding line 136 is in binary data
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84\x00\t\x06\x07\x13\x13\x12\x15\x12\x12\x12
\x15\x16\x15\x15\x15\x15\x17\x15\x15\x17\x15\x15\x15\x15\x15\x17\x15\x15\x17\x16\x15\x15\x15\x15\x18\x1d( \x18\x1a%\x1d\x15\x15
!1!%)+...\x17\x1f383-7(-.+\x01\n\n\n\x0e\r\x0e\x1a\x10\x10\x1b-%\x1f%---------------------+----------------------------\xff\xc0\
x00\x11\x08\x00\xc2\x01\x03\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1c\x00\x00\x01\x05\x01\x01\x01\x00\x00\x00\x00\x00\
x00\x00\x00\x00\x00\x02\x00\x01\x03\x04\x05\x06\x07\x08\xff\xc4\x00A\x10\x00\x01\x02\x03\x05\x03\t\x05\x06\x05\x04\x03\x00\x00\x00
\x00\x01\x00\x02\x03\x04\x11\x05\x12!1AQaq\x06\x13"2\x81\x91\xa1\xb1\xd1\x14BR\x92\xc1\x07#CS\xe1\xf0\x153b\x82\xb2r\xa2\xc2\xd2$%
D\xff\xc4\x00\x1a\x01\x00\x03\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\xff\xc4\x00*\x11
\x00\x02\x02\x01\x03\x04\x01\x04\x02\x03\x01\x00\x00\x00\x00\x00\x00\x01\x02\x11\x03\x131Q\x04\x12!Aa\x142q\xa1\x81\x91"\xe1\xf0B\
xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xd4lU3",\xf6\xbdN\xc8\x8b\xe9\xcf\x9d.\x82\x9c\xb0*\xec\x88\xac2 H\xa4V\x99\
x98\x86\xc75\x8f{Z\xe7\xe0\xc0M\x0b\x8e\x18\r\xb9\x8e\xf5#\xa0\xaek\x95o\x06rHl}{\xde\xcfE\xd6\xd5Lem\xa3W\x14\x92|\x94]\t\x0f6U\
xc2\xc4\xae*"\x8a<\xdaWU\xd2\xc4\x0e\x86\x80*\x90\x84\xb5N\xe6 p@\xc8(\x9d\x19L\x90\x03T\x93\x94\xc8\x01U$\xc9U\x00$\x8aj\xa5T\x80
b\x13\'\xaaH\x01\x80H\xb5\x12UL\x08\x8bP\x16\xab4@\xe6\xa5@V!\x01V\x1c\x14e\xaahdI\'sP\x94\x00\x91\xb5Ey\x03\xa6\x1a3sGhJ\xc5E\xba
\xa4\xa8\xfb|?\xccg\xcc\xdfT\xe9\xf7 \xedf\x88(\xda\xe5\x08F\x15\xd9\x14Yk\xd4\xcd\x88\xaa4\xa9\x01N\xc2\x8e{\x94 >zU\xa7\x11\xd1
\?\xef\xaf\xd1u\xc1\xeb\x8e\xb4\xdd[B\x06\xe6\xb7\xcd\xcb\xack\x96X\xf7\x97\xe4\xda\x7fl\x7f\x04\xe1\xc8\x83\xd4\x15MyhfX\xe7\x12\
\xbe\xa0\xbc\x98\xb9\x03\xb2g\x10\x84\x80\xaa\xbem\x837\xb4v\x85\x13\xed&\x0cjO\x06\xb8\xfd\x12\xb4:e\xb7BQ\xba\x1a\xacm-\x8cw\xf
bG\xd5G\xfcE\xc4\x90\x180\xda\xef@\x8e\xe4\x14\xcbe\xa8\n\xa7\x1an%\t\xab\x05\x07\xc2O\xd5\x0b\xdc\xf3\xf8\x87\xb04}\x12\xee\n.\
x12\x9c,\x97\x8e\x90\xab\xddJ\x1fx\x8dF\xcao@\xf8\x90GY\xcd\xfe\xe7W\xcc\xa9\xef\x1fi\xac\xf7\x81\x99\x03\x89\n#5\x0f\xe3oa\x07\
xc9e\xc3\x9b\x82\xdb\xc6\xad\x18\xe1A\xb8lI\xd6\xd4\x10ix\x9e\r*u\x17%i\xbe\x19\xa3\xed\x8c\xd2\xa7\x83\\|h\x97\xb5\xecc\xcf`\x1e
d,\x98v\xd402v\xba\rMv\xa0u\xbe\xdd\x18{H\tj\xc7\x91\xe9K\x82\xd5\xa3l\xba\x19\x86\xd1\x08\xd5\xee\xa6.\x03\x0c\x018Wj\xb8c\xc4\x
f8\x1b\xf3\x9f\xfa\xaeN\xd6\xb4\xf9\xc7\xc2u\xda\\5\xce\xb5\xc4\x1d\x9b\x95\xd7\xf2\x81\xfa1\xbe%F\xb2\xb7\xe4\xd1\xe1t\xa9\x1b\x
e24O\xe8\x1d\x8e?P\x86\x14h\x8eh%\xcd\x15\x00\xe0\xcd\xbcJ\xe7\xcd\xb9\x17c{\x8f\xaa\x83\xf8\xbcP\x00\x0e\xc8\x01\xd5\x1a#^?"\xd0
\x97\xc1\xd3\x96\xb8\xfe#\xbb\x03?\xea\xa0\x8e\xc3O\xe6?6\x8c\xc0\xcd\xc0h7\xaem\xf6\xb4_\xcc\xf0o\xa2\x81\xf6\xa3\xceqN\x9e\xf52
'''