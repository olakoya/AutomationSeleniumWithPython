'''
Diamond Problem
----------------
If the same method is inherited from both parent classes (Multiple Inheritance), it creates ambiguilty about which method the 
child class should use.

MRO (Method Resolution Order)
-----------------------------
To get the order for Diamond Problem we need "mro() method"
The mro follow a particular principle which is called DLR

DLR means Dept First Left to Right e.g
If a class C(P1,P2) is executed ==> P1 will be considered first
If a class C(P2,P1) is executed ==> P2 will be considered first

A Parent class can't be called or accessed bferoe a child class
E.g
'''
class A:
    # def process(self):
    #     print("A process")
    pass

class B:
    def process(self):
        print("B process")

class C(A,B):
    # def process(self):
    #     print("C process")
    pass

c = C()
c.process()
# print(C.mro())
'''
C process
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

After commenting out lines 35, 28 and 29 out and adding 'pass' to the code in line 30 the output became
A process

And when I comment out lines 20 and 21 and add a 'pass' in line 22 and execute the code again the output is
B process
'''
# E.g 2
class A:
    # def process(self):
    #     print("A process")
    pass

class B(A):
    def process(self):
        print("B process")

class C(A,B):
    pass

# c = C()
# c.process()
print(C.mro())
'''
Output is TypeError because a parent class was called before a child's class which should never be
Traceback (most recent call last):
  File "/Users/olakoya/Desktop/automationwithpython/Day26/Diamond_Problem.py", line 56, in <module>
    class C(A,B):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B

A class can't called it's class which is a violation of the principle except for cyclist inheritance
'''
#-------------------------------------------------------------------

'''
Super Method()
---------------
This is to call super or parent class members (constructors or methods or variables) from child class
E.g
'''
class A:
    def process(self):
        print("A process")

class B(A):
    def m1(self):
        super().process() # super is a method and this line of code is for modification

b = B()
b.m1()
'''
Output is 
A process

we can access parent class method or modifiy any functionality by using super method
'''
# E.g 2

class Bank:
    def rateofinterest(self):
        return 0
    
class XBank(Bank):
    def m1(self):
        return super().rateofinterest()+10

class YBank(Bank):
    def m2(self):
        return super().rateofinterest()+12
    
ybank = YBank()
ybank.m2()
    