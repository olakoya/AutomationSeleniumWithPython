# Simple if conditional statement
# --------------------------------
'''
"if" is one of the keyword python
Before the condition there's a variable (x)
E.g
'''
# x = 10 # x is a value while 10 is the variable
# if x>5: # inside "if" body the condition can have multiple statement. We're also passing the x value inside the "x>5 memory location"
#     print("x is greater than 5") # Output is "x is greater than 5"
# else:
#     print("x is less than 5")

# name = input("Enter Name = ")
# if name == "Ola": # Using this "equality == operators" for comparison and to check if the statement is true
#                  # But when use single '= operator' it is seen as an assignment of a value
# # We use if to validate the statement as it's added above"
#     print("Hello Ola, Good Morning")
# print("How are you?") #storing a data inside variable
'''
Output is;
Enter Name = Ola
Hello Ola, Good Morning
How are you?

2nd run Output with a different name input
Enter Name = Mike
How are you?
'''
# When using the conditional statement one needs to specify ":" colon after the "if statement" otherwise it will give SyntaxError
# SyntaxError needs to be corrected by a Developer

# if-else conditional statement
# ------------------------------
# y = 3 # Variable "y" and Value is "3"
# # Checking if y is an even number and to check a reminder modular division "%" operator will give a reminder
# if y%2 == 0:
#     print("Even Number") 
# # if action 1 is true action 2 will be executed
# else:
#     print("Odd Number")
# # Output is Odd Number

# name = input("Enter Name = ")
# if name == "Ola": # Using this "equality == operators" for comparison and to check if the statement is true
#                  # But when use single '= operator' it is seen as an assignment of a value
# # We use if to validate the statement as it's added above"
#     print("Hello Ola, Good Morning")
# else:
#     print("Hello Guest Fine Morning")
# print("How are you?") #storing a data inside variable
'''
Output is;
Enter Name = Gus
Hello Guest Fine Morning
How are you?
'''

# if-elif-else conditional statement
# ----------------------------------
# marks = 65 
# # we want to check grades of student base on marks
# if marks>=90:
#     print("A Grade")
# elif marks>=80:
#     print("B Grade")
# elif marks>=70:
#     print("C Grade")
# else:
#     print("He is Failed") # default action specify in the else block
'''
Output when used 75 for varaible is 
C Grade

Output at 2nd execution after add the last "else" which is the default action and changing variable number to 65
He is Failed
'''

# # How to read some favorite brand name from the user by using the input method?
# brand = input("Enter Your Favourite Brand: ")
# if brand == "RC":
#     print("This is Children's brand")
# elif brand == "KF":
#     print("It is not that much kick")
# elif brand == "FO":
#     print("Buy one get one free")
# else:
#     print("Other brands are not recommended")
'''
Output 1 is
Enter Your Favourite Brand: MK
Other brands are not recommended

Output 2
Enter Your Favourite Brand: KF
It is not that much kick

Output 3
Enter Your Favourite Brand: FO
Buy one get one free

Output 4
Enter Your Favourite Brand: RC
This is Children's brand
'''

# nested if-else conditional statement
#-------------------------------------
num = 0 
# We need to check if the number is +ve or -ve or zero or even or odd
if num>0: # ie if condition num is true print +ve number
    if num%2 == 0:
        print("Positive and even number")
    else:
        print("Positive and even number")
elif num<0:
    print("Negative number")
else:
    print("Zero number")
'''
Output 1 for value 15
Positive and even number (because it's not divisable by 2)

Output 1 for value -15
Negative number

Output 1 for value 0
Zero number
'''