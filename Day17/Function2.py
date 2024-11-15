'''
Functions in Python
--------------------
Function is a group of statements upon calling performs certain task.

'''

# a, b # a, b are variables and inside of it i will store some data

# def add_elements(a,b): # to sepecify name of the above we then add element and taking two pararmeters a and b

#     sum = a+b # add some value using sum to the variable (variable name)

#     print(sum) # this is printing out the sum

'''
Defining the above ==> (sum = a+b) and (print(sum)) as a group and the group is called function

So, how to define function from the above codes;
------------------------------------------------
1. we have the def keyword ==> def
2. Follow by function name ==> add_elements
2a. The combination of the above two is called function ==> def add_elements(a,b):
3. Then open and close parenthesis ==> () 
4. Inside parentehsis we have the variables a and b which are parameters ==> (a and b)
5. And then the group statements ==> (sum = a+b) and (print(sum))
6. When we call the function ==> (def add_elements(a,b):) it will perform the group name ==> (sum = a+b) and (print(sum))
'''
'''
Types of Functions are
1. Buit-in
2. User defined functions
    i. def function_name(parameters):
    ii. "doc string"
    iii. group of sttatements
    iv. return result
3. function_name(parameters): these are optional
Function can take parameters and can take in data and this are called arguments
Parameters ==> inputs ==> values ==> Arguements
'''
# No Arguements and No Return value => this is optional parameters
#-----------------------------------------------------------------

# def myfun(name):
#     print("Hello")
# myfun("Ola")

'''
Output is
Hello
'''
# Parameters are also variables

# No Arguements and No Return value => this is optional parameters
#-----------------------------------------------------------------
def myfun(name):
    print("Hello", name)
print(myfun("OLA"))
myfun("PRADEEP")
'''
Output is
Hello OLA
None
Hello PRADEEP
'''