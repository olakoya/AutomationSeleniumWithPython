# Interactive Statements
# -----------------------
# For notes to support the below codes, check Day 3 Control Statement Notes File

# while loop
# print numbers from 1 to 10
#-----------------------------
i = 1 #initialisation i = 1
# after while you need to start a condition
while i<=10: # after using color : it will be treated as a valid syntax
# inside the while body you're specifying multiple statements and in this case I want to print an increment value
# "while i<=10" is a condition i = 1 2 3 ...... 11
    print(i) # if the above statment is true it will print the statment 1 2 3 4.....10
    i = i+1 # increment # i = 2 3 4 ..... 11
# Based on condition is printing the numbers
'''
Output is
1
2
3
4
5
6
7
8
9
10
'''
# print numbers from 10 to 1
#------------------------------
i = 10 # initialisation
while i>=1: # Condition i = 10 9 8 7 .... 1
    print(i) # print 10 9 8 7 .... 1
    i = i-1 # Decrement # i = 9 8 7 ....1 0
'''
Output is
10
9
8
7
6
5
4
3
2
1
'''

# display sum of first n number
#--------------------------------
# n is a dynamic number and can be converted into interger
n = int(input("Enter Number : ")) # 5 "input("Enter Number : ")" any number entered into "input" will be treated as string datatype 
# however, to convert the string into integer "int" is added to the code "int(input("Enter Number : "))" 
# adding "n" is to store a number and it is added to the line of code i.e. "n = int(input("Enter Number : "))""

# To solve the above problem i.e. the n line of code we need to use a while loop and number can be 0
sum = 0 # sum isn't initialiazation but a variable where the numbers will be stored
i = 1 # initialisation (1 is where the number start counting from) and to specify the condition "while loop" is used
while i<=n: # condition i value increases = 1 2 3 4 5 6
    sum = sum+i # i value add data 1 3 6 10 15
    i = i+1 # increment #i = 2 3 4 5 6
print(sum)
'''
Output 1
Enter Number : 5
15
Output 2
Enter Number : 10
55
Output 3
Enter Number : 100
5050 # total number of the 1 to 100 numbers
'''

#prompt user to enter name until entering Neel
#----------------------------------------------
# We implement this by using while loop statements
# We need to have name variable
# Neel is a requirements name
# To promtp user to add name and we need to have condition 
name = " " # name has an empty variable " "
while name!="Neel": # This is condition "is not" 
    name = input("Enter Name = ") # prompting of variable
'''
Output is
Enter Name = Ola
Enter Name = MK
Enter Name = Angel
Enter Name = Neel
'''
# Adding simple message
print("Thanks for confirming")
'''
Output is
Enter Name = Pj
Enter Name = Mk
Enter Name = Pujab
Enter Name = Rishi
Enter Name = Neel
Thanks for confirming
'''