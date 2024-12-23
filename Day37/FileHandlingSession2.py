'''
File Handling Session 2
------------------------
To perform any operation one needs to specify:
1. Open(filename, mode)
2. Actions
3. Close()

An operation must always close the file at the end of each operation and without which it will be impossible to save and
might encounter have issue.

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
# with the help of f = open variable one would be able to perform this operation ("abc.txt", "w") as seen below
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

The 'true' output displayed that the execution is closed
'''

# not issuing any close generally it might write some exceptions or issues or exceptions
# Lines 36 to 38 will specify the closure and to close line 39 will be used
'''
Without close() method below might happened
--------------------------------------------
Exceptions is that file will not properly closed
There maybe chance of missing some data while
Close () must be specify all the time
'''