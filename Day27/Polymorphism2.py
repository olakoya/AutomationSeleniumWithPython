'''
2. Overloading Philosophy
---------------------------
This is the ability to use the same operators or methods for different purposes with different implementations

    i. Operator Overloading
    ------------------------
    This is using the same operator for multiple purposes.
E.g
'''
print(10+20)
print('Micro'+"Soft")
'''
Output is 
30
MicroSoft

E.g 2
'''
print(10*3)
print("Microsoft"*10)
'''
Output is 
30
MicrosoftMicrosoftMicrosoftMicrosoftMicrosoftMicrosoftMicrosoftMicrosoftMicrosoftMicrosoft
'''
#---------------------------------------------------------

'''
    ii. Method Overloading
    ------------------------
    This is the same method with different implementations for multiple purposes
E.g
'''
class Test:
    def m1(self):
        print('no-arg method')

    def m1(self,a):
        print('one-arg method')

    def m1(self,a,b):
        print('two-arg method')

#     def m1(self,*a): # variable number of arguements
#         print(a)
    
# def m1(self,a=None,b=10,c=20): # default arguemnets
#     print(a,b,c)

t = Test()
t.m1(10,20)
'''
Output is
two-arg method

and after adding lines 45 to 49, output is
(10,20)
'''
#--------------------------------------------------------------

'''
    iii. Constructor Overloading
    -----------------------------
    This is the same constructor with different implementations for multiple purposes
E.g
'''
class Test:
    def __init__(self):
        print('No arg constructor')

    def __init__(self,a):
        print('One arg constructor')

    def __init__(self,a,b):
        print('Two arg constructor')

Test(10,20)
'''
Output is
Two arg constructor
'''