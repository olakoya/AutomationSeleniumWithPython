# Checkout Day 19 Class_Object_Notes for more Inheritance Notes
'''
Inheritance in Python
-----------------------
It is using members of one class inside another class. This is possible by;
    i. Composition (HAS-A Relationship)
    ii. Inheritance (IS-A Relationship)

Thypes of Inheritance in Python;
----------------------------------
1. Single Inheritance 
    Class A (Parent) <---- Class B (Child)

2. Multilevel Inheritance 
    Class A (Grand-Parent) <----- Class B (Parent) <---- Class C (Child)

3. Hierarchical Inheritance 
                     <---- Class A (Child)
    Class A (Parent) <---- Class B (Child)
                     <---- Class C (Child)

4. Multiple Inheritance 
    Class A (Parent)
                       \
                         <---- Class C (Child)
                        /
    Class B (Parent)

5. Hybrid Inheritance 
              Class A (Grand-Parent)
                    /       \
    Class B (Parent)        Class C (Parent)
                    \       /
                 Class D (Child)



The reasons of Inheritance in Python are;
i. Code Reusability
ii. Avoid Duplication
iii. Development Time also Reduced

E.g

Without using Members                                   |                          With using Members
---------------------------------------------------------------------------------------------------------------------
1. Class PersonalLoan:                                  |                          1. Class Loan:
    // 50 Methods                                       |                               // 30 Common Methods
2. Class HomeLLoan:                                     |                           2. Class PersonalLoan(Loan):
    // 50 Methods                                       |                               // 20 Common Methods
3. Class VehicleLLoan:                                  |                           3. Class HomeLoan(Loan):
    // 50 Methods                                       |                               // 20 Common Methods
                                                        |                           4. Class VehicleLoan(Loan):
                                                        |                               // 20 Common Methods
Total Methods = 150 methods                             |                           Total Methods = 90 methods 
Total Development time = 150 Hours                      |                           Total Development time = 90 Hours

By Composition (HAS-A Relationship)
------------------------------------
1. By using classname or object reference variable one can access members of one class inside another class

'''
# E.g Creating an object inside another class
class A: 
    c = 10 # class variable
    def __init__(self): # constructor
        self.d = 20 # instance variable
    def m1(self): # instance method
        print("This is method class A") # calling class A

# below is how to access the above class, and it's by creating an object of class A
class B:
    def __init__(self):
        self.a = A() # this object reference variable is an instance variable
    def m2(self):
       self.a.m1() # accessing a method of class
       print(self.a.d+self.a.c)

b = B()
b.m2()

'''
Output is
This is method class A
30
'''
