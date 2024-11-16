'''
Functions in Python
--------------------
1. If a group of statements is repeatedly required then it is not recommended to write these statements everytime seperately.
E.g
The below 3 code statements aren't required and they are all doing addition statements;
'''
a = 10
b = 5
print(a+b)
'''
Output is 15
'''
c = 100
d = 250
print(c+d)
'''
Output is 350
'''
e = 79
f = 47
sum = e+f
print(sum)
'''
Output is 126
'''
'''
2. We have to define these statements as a single unit and we can call that unit any number of times based on our requirements 
without rewriting the code. This unit is nothing but functions.

3. The main advantage of functions is for code relaibility and to avoid duplication.

4. In other languages functions are known as methods, procedures, subroutines etc.

5. Function and Method are different in python.

6. After learning this function it will be easy to understand Object Oriented Programming (OOP) Language
'''
def add_element(a,b):
    sum = a+b
    print(sum)
# Group name is called a function name

'''
1. def add_element(a,b): ==> This is a call declaration
2. add_element ==> This is a function call
3. (a,b) ==> This function is accepting two parameters a and b
4. If the function (a,b) is accepting some input, Parameters are nothing but input
5. Whenever you are calling a function you need to 


'''