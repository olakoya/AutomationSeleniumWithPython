# print(self, *args, sep=' ', end='\n', file=None). These are parameters operators
# ------------------------------------------------
# *args is used to print arg value. It can pass mulitple arguement. print functions will seperate them
# seperate will seperate functions e.g

# args means arguement
# ---------------------
print("Hello", "World") # space is used to seperate the words
# seperated aparameters value and passings value to the parameters by adding "sep="+"" to the above code
print("Hello", "World", sep="+") # "sep="+"" can be used for any number of values
'''
Output for the above 2 codes are
Hello World
Hello+World
'''

# sep means seperate
# ---------------------
# string inserted between values, default a space.
# Other operators can be used e.g
print("Hello", "World", sep="-") # mutltiple values
print("Hello", "World", sep="=")
'''
Output for the above 2 codes are
Hello-World
Hello=World
If you want to add string, it is used in separate parameters
'''

# end means add data at the end of the statement
# -----------------------------------------------
'''
end parameter will pass value
string appended after the last value, default a newline e.g
'''
print("Hello", "World", end="=")
'''
Output is
Hello World=
'''
print("Hello", "World", end="\t")
'''
Output is
Hello World
'''
print("Hello" , "World" ,end="\n")
'''
Output is 
Hello World
'''
print("Hello","World" ,end="\n") # '\n' means a new line in the execution
'''
Output is 
Hello World
'''
print("Hello","World" ,end="*") 
'''
Output is 
Hello World*
Between the values "Hello World" string is seperated, and after the value there's end parameter and its value
'''
print("Hello","World" ,end="*") 
print("This is my python language")
'''
Output is
Hello World*This is my python language
Above output is from the code of the two printed statements
'''
print("Hello",end="x")
print("World")
'''
Output is
HelloxWorld
'''

# file=None
# -----------
# This can specify file location
# This is a file like object (stream); defaults to the current sys.stdout.
# That is, helping to write a data into a specific file

with open("output.txt1", "a") as f:
    f.write("Hello world !\n") # This is use to write into a new line
    print("Hello World!", file=f) # This is use to write into a specific file
print("Script executed")
'''
Output in output.txt1 is
Hello world !
Hello World!
Hello world !
Hello World!
Hello world !
Script executed
'''
with open("output1.txt", "a", encoding="utf-8") as f:
    f.write("Hello world !\n")
    print("Hello World!", file=f)
print("Script Executed")
'''
Output in output1.txt is
# Hello World!
Script Executed
'''
with open("output.txt", "w") as f:
    f.write("Test line \n")
print("Script Executed")
'''
Output displayed in output.txt is
Test line 
Script Executed
'''
# /t means two spaces between two values
print("Hello",end="\t")
print("World")
'''
Hello   World
'''
print("Hello",end="\\")
print("World")
'''
Hello\World
'''
print("Hello",end="\r")
print("World")
'''
World
'''
print("Hello",end="\f")
print("World")
'''
Hello
     World
'''
print("Hello","World",end="\f")
print("We are learning Python")
'''
Hello World
           We are learning Python
'''
print("Hello","World",end="\\")
print("We are learning Python")
'''
Hello World\We are learning Python
'''
print("Hello","World",end="\n")
print("We are learning Python")
'''
Hello World
We are learning Python
'''
with open("output1.txt", "a") as f:
    f.write("This is Ola \n") # using write method to execute the statement
print("Script Executed") # This is the standard output object
'''
Output displayed in output1.txt is
This is Ola 
Script Executed
'''
with open("output1.txt", "a") as f:
    f.write("Creating a new text file makes it work\n") # using write method to execute the statement
print("Script Executed") # This is the standard output object
'''
Output displayed in output1.txt file
Creating a new text file makes it work
Script Executed
'''
with open("output1.doc", "a") as f:
    f.write("Creating a new text file makes it work\n") # using write method to execute the statement
print("Script Executed, ")
