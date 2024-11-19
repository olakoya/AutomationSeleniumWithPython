'''
Functions in Python
--------------------
Function is a group of statements upon calling to perform certain task.
It is also an entry point.

'''

# a, b are variables and inside of it will store some data

def add_elements(a,b): # to sepecify name of the above variables '(a,b)' we add '(add_element)' and taking two pararmeters '(a and b)'

    sum = a+b # add some values using 'sum' to the variable (variable name)

    print(sum) # this is printing out the sum

'''
Defining the above "(sum = a+b) and (print(sum))" as a group and the group is called function

So, how to define function from the above codes;
------------------------------------------------
1. we have the def keyword ==> def
2. Follow by function name ==> add_elements
2a. The combination of the above two is called function ==> def add_elements(a,b):
3. Then open and close parenthesis ==> () 
4. Inside the parenthesis we have the variables a and b which are parameters ==> (a and b)
5. And then the group statements ==> (sum = a+b) and (print(sum))
6. When we call the function ==> (def add_elements(a,b):) it will perform the group name ==> (sum = a+b) and (print(sum))
7. Value pass to the parameters during run time is called arguement
'''
'''
Types of Functions are
-----------------------
1. Buit-in
2. User defined functions
    i. def function_name(parameters):
    ii. "doc string"
    iii. group of statements
    iv. return result
3. function_name(parameters): these are optional
Function can take parameters and can take in data and this are called arguments
Parameters ==> inputs ==> values ==> Arguements
'''
# 1. No Arguements and No Return value 
#--------------------------------------
# => this is with optional parameters

# E.g. 1
def func():
    print("Hello")
func()

'''
Output is
Hello
'''

# E.g. 2
def func():
    print("Hello")
print(func())

'''
Output is
None
'''
# Parameters are also variables

# 2. With Arguements and No Return Value or Result
#--------------------------------------------------
# E.g. 1
def myfun(name):
    print("Hello", name)
myfun("Ola")
myfun("Nadine")

'''
Output is
Hello Ola
'''

# E.g. 2
def myfun(name):
    print("Hello", name)
print(myfun("OLA"))
myfun("PRADEEP")
'''
Output is:
Hello OLA
None
Hello PRADEEP
'''

# 3. With Arguements and With Return Value or Result
#------------------------------------------------
# E.g 1
def myfun(name):
    return "Hello", name

print(myfun("Ola"))
'''
Output is
('Hello', 'Ola')
'''

# E.g 2
def myfun(name):
    return "Hello "+name

print(myfun("Ola"))
'''
Output is
Hello Ola
'''

# E.g 3
def myfun(name):
    return "Hello "+name

myfun("Ola")

'''
Output is
None
'''

# 4. No Arguements and With Return value 
#----------------------------------------
# E.g 1
def fun():
    return 10
x = fun()
print(x)
'''
Output is
10
'''

# E.g 2
def fun():
    return 10
print(fun())
'''
Output is
10
'''

# E.g. 3 
def fun():
    return 10
fun()
'''
Output is
None
'''