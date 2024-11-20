# Types of Variables
# -------------------
'''
1. Global Variables: It declared outside a function and accessible in all functions of the module.
2. Local Varaibles: It declared inside a function and accessible only within that function.
3. Global Keyword: It used to declare or modify a global variable inside a function.

x = commondata ==> Global variable

Below are models and inside of it contains some functionalities

def login () ==>  login functionality
        y = uncommondata # local variable

def logout() ==>  logout functionality
        z = uncommondata ==> storing commodata z

def register() ==>  register functionality
        i = uncommondata ==> storing commodata i

def signup() ==>  signup functionality
        j = uncommondata ==> storing commodata z
    
n functionalies ==>  till infinity functionalities

1. When implementing an application there could be any number of functions
2. And these functions i.e. the above functions are been defined in a model inside a python file (.py file)
3. Each function has a common data i.e specify(... = commodata) and with that we define a variable i.e. x
4. Each time the data is changed, we go into the variable and change the data via declaring a GLOBAL VARIABLE (x = commodata)
5. And once global variable (x = commodata) is declared and it then can be access by each function(def login, logout, register etc)
6. If there's a data different from the avaiable function to function it becomes uncommondata and this is called LOCAL VARIABLE
7. And this y = uncommondata is define/created in this particular function (def login) only and this applies to other def function too
8. i = uncommodata is only responsible/property for register functionality and not for signup functionality and vice versa
9. Once we define any LOCAL VARIABLE it's only bond to that particular function in which it is declared i.e. def login(), y = uncommodata
10. Once we define a GLOBAL VARIABLE, it can be accessed by the every function of a particular module i.e def login, ded logout, def register etc
11. Module is different, function is differen, library is different and class is different
'''
'''
Function ==> Is a group of statements
Module (.py file) ==> is a group of functions saved to a file and also a python file
Selenium ==> is a library and inside of it is webdriver 
Library/Package ==> Is group of Modules
'''

# Local and Global Variables
# ---------------------------
# E.g

a = 10 # Global Variable

def add ():
    b = 20 # Local Variable 
# To make c function as a global keyword it has to be created inside of a function
    global c # Global variable 
    c = 30 # Local variable because it's created inside a function and inside keyword
    print(a+b)

def sum():
    print(a+c)

add()
sum()
'''
Output is
30
40
'''

