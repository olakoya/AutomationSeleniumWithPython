# print(self, *args, sep=' ', end='\n', file=None). These are parameters operators
# ------------------------------------------------
# *args is used to print arg value. It can pass mulitple arguement. print functions will seperate them
# seperate will seperate functions e.g

# args means arguement
# ---------------------
# print("Hello", "World") # space is used to seperate the words
# # seperated aparameters value and passings value to the parameters by adding "sep="+"" to the above code
# print("Hello", "World", sep="+") # "sep="+"" can be used for any number of values
'''
Output for the above 2 codes are
Hello World
Hello+World
'''

# sep means seperate
# ---------------------
# string inserted between values, default a space.
# Other operators can be used e.g
# print("Hello", "World", sep="-") # mutltiple values
# print("Hello", "World", sep="=")
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
# print("Hello", "World", end="=")
'''
Output is
Hello World=
'''
# print("Hello", "World", end="\t")
'''
Output is
Hello World
'''
# print("Hello" , "World" ,end="\n")
'''
Output is 
Hello World
'''
# print("Hello","World" ,end="\n") # '\n' means a new line in the execution
'''
Output is 
Hello World
'''
# print("Hello","World" ,end="*") 
'''
Output is 
Hello World*
Between the values "Hello World" string is seperated, and after the value there's end parameter and its value
'''
# print("Hello","World" ,end="*") 
# print("This is my python language")
'''
Output is
Hello World*This is my python language
Above output is from the code of the two printed statements
'''
# print("Hello",end="x")
# print("World")
'''
Output is
HelloxWorld
'''

# file=None
# -----------
# This can specify file location
# This is a file like object (stream); defaults to the current sys.stdout.
# That is, helping to write a data into a specific file

# with open("output.txt", "a") as f:
#     f.write("Hello world !\n")
#     print("Hello World!", file=f)
# print("Script executed")
'''

'''
# with open("output.txt", "a", encoding="utf-8") as f:
#     f.write("Hello world !\n")
#     print("Hello World!", file=f)
# print("Script executed")

with open("output.txt", "w") as f:
    f.write("Test line\n")
print("Script executed")
