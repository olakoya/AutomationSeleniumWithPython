'''
File Handling in Python
-------------------------
File is used to store files permanently i.e used as permanent storage areas to store data
We use it for Data Driven Testing.

Types of Files available
-------------------------
1. Text file is used to store character data
2. Binary Files is used to store binary data

To handle any file firstly one needs to open the file
i. Opening the File
----------------
Open it in ==> filename and mode (r: read only, w: write only, a: append, r+: read and write, w+: write and read etc)

Once file is opened an operation will be performed
ii. Closing the file
--------------------
Close with open and close brackets ()

iii. Variable properties of the File
--------------------------------------
That is the name of the file
    mode
    closed
    readable()
    writeable()
All the above properties are called methods
E.g
'''

# 1st - open the file in write mode
f = open("abc.txt",'w')

# assign variable f above to perform

# getting name of the file
print(f.name)

# which mode the file is opened
print(f.mode)

# checking if it is readable
print(f.readable())

# checking if it is writable
print(f.writable())

# checking if it is close
print(f.closed)

# closing the file
f.close()
print(f.closed)

'''
Output is 
abc.txt ==> name of the file
w ==> mode file is opened
False ==> file isn't readable because we only have 'w' in line 34 method
True ==> file is writable as declared in line 34
False ==> file is not closed

Adding lines 54 and 55

Output is 
.......
True
Process finished with exit code 0

Above codes and outputs show one can read and write contents
'''

'''
Writing Data to a File
------------------------
1. One need to open the file in the write mode only
E.g
'''
# write data to the file
f = open("abc.txt",'w') # to be able to write one needs to open it in 'w' mode
# followed by write method
f.write("Learning Python is very easy")
# open the file, perform the operations and close
f.close()

'''
Output is
Learning Python is very easy ==> is displayed in the abc.txt file

--------------------------------------------------------
To write in a new line one needs to specify in the code
E.g
'''
f = open("abc.txt",'w')
f.write("Learning\nPython\nis\nvery\neasy") # adding \n is to write in a new line accordingly
f.close()
'''
Output is that it's overwrite the previous execution in lines 82 to 86 and from output in line 90 to the one below
Learning
Python
is
very
easy
'''
# adding data to existing file rather than overwriting it
f = open("abc.txt", 'a') # adding append 'a' mode will add data to existing data rather than overwriting it
f.write("\nLearning\nPython\nis\nvery\nvery\neasy")
f.close()
'''
Output is 
Learning
Python
is
very
easy
Learning
Python
is
very
very
easy

------------------------------------------
How to Read character Data from Text Files
-------------------------------------------
There are specific method to do that;
1. read() ==> will read total data from the file
2. read(n) ==> will read number of lines 'n' characters from the line
3. readline() ==> will read only one line
4. readlines() ==> will read all lines in the list

Supposing one tries to write data in another text file in a different folder like Day 27
i. Openned Day27 directory
ii. Create the text file in the directory
iii. Betterstill creating a file that doesn't exist automatically during execution time
E.g
'''
f = open("test.txt", 'a') # adding append 'a' mode will add data to existing data rather than overwriting it
f.write("\nLearning\nPython\nis\nvery\nvery\neasy")
f.close()
'''
Output is that a testingfile.txt file was created automatically in Day36 directory during run time as seen on screenshot
Learning
Python
is
very
very
easy
'''
#--------------------------------------------------------
'''
Below is how to read contents "Learning Python is very easy" written in testingfile text file located in Day27 directory
E.g
'''
open("testingfile.txt",'r')
print(f.read())
f.close()

'''
Output is an exception error
line 157, in <module>
    open("testingfile.txt",'r')
FileNotFoundError: [Errno 2] No such file or directory: 'testingfile.txt'

#--------------------------------------------------------
To get a successful execution path location is required and to get that right click on the testingfile file and copy absolute path

/Users/olakoya/Desktop/automationwithpython/Day27/testingfile
E.g
'''
f = open(r"/Users/olakoya/Desktop/automationwithpython/Day27/testingfile",'r')
print(f.read())
f.close()
'''
Output displayed on terminal is
Learning Python is very easy
Learning Python is very easy
Learning Python is very easy
Learning Python is very easy
Learning Python is very easy
'''

#--------------------------------------------------------
# Reading first 10 characters
f = open(r"/Users/olakoya/Desktop/automationwithpython/Day27/testingfile",'r')
print(f.read(10))
f.close()
'''
Output is
Learning P
'''

#--------------------------------------------------------
# Reading only a line
f = open(r"/Users/olakoya/Desktop/automationwithpython/Day27/testingfile",'r')
print(f.readline())
f.close()
'''
Output is
Learning Python is very easy
'''

#--------------------------------------------------------
# Reading multiple lines
f = open(r"/Users/olakoya/Desktop/automationwithpython/Day27/testingfile",'r')
print(f.readlines())
f.close()
'''
Output is 
['Learning Python is very easy\n', 'Learning Python is very easy\n', 
'Learning Python is very easy\n', 'Learning Python is very easy\n', 'Learning Python is very easy']
'''