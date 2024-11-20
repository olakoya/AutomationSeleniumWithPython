'''
Types of Arguements
--------------------
1. Positional
2. Keyword
3. Default
4. Variable Length
5. Keyword Variable Length

'''
# 1. Positional Arguements
# ----------------------
'''
This is arguements passed in correct order
Changing order or changing number of arguements will return an error or incorrect results
'''
# E.g
# def func(a,b): # first you define a function
#     print(a/b) # simple statement 

# func(10,5) # calling functions, passing values and calling the arguements
# func(5,10)
# func(10,5,12)
'''
Output is 
2.0
0.5
Traceback (most recent call last):
  File "/Users/olakoya/Desktop/automationwithpython/Day17/Functions2.py", line 23, in <module>
    func(10,5,12)
TypeError: func() takes 2 positional arguments but 3 were given
'''

# 2. Keyword Arguements
# ----------------------
'''
These are arguements passed using parameter names
Order isn't important but number of arguement is important
'''
# E.g
# def func(a,b): # first you define a function
#     print(a/b) # simple statement

# func(a=10,b=5) # with help of parameters i'm passing the value
# func(b=5,a=10) # order isn't important
'''
Output is
2.0
2.0
'''

# 3. Default Arguements
# ----------------------
'''
This is to assign default values to parameters
If no value is passed during function call default value is taken
'''
# E.g
# def func(a=10,b=5): # first you define a function and assign default value arguement
#     print(a/b) # simple statement

# func()
# func(15)
# func(100,200)
'''
Output is
2.0 printing result without passing value func() but passed result from the default values
3.0 printing result with a passing value func() but passed result from the default values
0.5
If a value isn't passed when calling function, this default function func(a=10,b=5) will be considered
And this is useful print(a/b) when there's no input 
'''

# 4. Variable Length Arguements ==> *n
# -------------------------------------
'''
This allows passing of any number of arguement including zero number
These are stored in the form of tuple ==> (1,2,3), this arguement is true
'''
# E.g
# def sum(*n): # *n is the number of variable to pass
#     total = 0 # simple statement
#     for n1 in n: # print of number of arguement i.e. tuple(1,2,3)
#         total = total+n1 # adding "total = 0" and "for n1 in n" together
#     print(total) # printing the total sum of all the arguement

# sum () # calling the function with the total number of arguement
# sum(10) # passing arguement
# sum(20,30) # i.e. *n: 20, 30
# sum(10,20,40,60,70,80,80) # i.e. *n: 10,20,40,60,70,80,80
'''
Output is 
0 total = total 0 + n1 0 => print 0
10 total = total 0 + n1 10 => print 10
50 total = total 0 + n1 50 => print 50
360 total = total 0 + n1 10+20+40+60+70+80+80 => print 360

Number of varaibale can be specify with * and a letter
'''

# IMPORTANT NOTES
# -----------------
'''
1. Position arguements must come first
2. Non-Default comes before default
3. Variable-length arguments can mix with positional
4. Arguements after variable-length must be keyword only
'''

# 5. Keyword Variable Length Arguements ==> **kwargs
# ---------------------------------------------------
'''
These are stored in form of Dictionary 
And in the dictionary we have ==> Key and value pairs e.g (key 1, Value 1), (key2, value 2)
The arguements are represented in the form of dictionary
And it can be represented by using double star kwargs i.e. **kwargs
**kwargs is the arguement name whenever we are declaring a function
** means keyword variable length arguement
kwargs means kw ==> keyword, args ==> arguements and both combined is called kwargs
'''
# E.g
def display(**n): # declaring a function
    for k,v in n.items(): # using for loop for k,v in dictionary n.item (n values while n is dictionary and it will only return dictionary)
    # when one use value it will return only value and if it's item used it will return kwargs i.e k and v
        print(k,v) # print key k and it's value v
# Whenever we are declaring a function "def display(**n):" 
# and this function is having a requirement to take input "for k,v in n.items()" as a dictionaryits then make "**n"
display(n1=10, n2=20, n3=30)
'''
Output is
n1 10
n2 20
n3 30

One can also use variable inside functions 
And variables are not parameters
'''
