'''
Inheritance
------------
1. Inheritance is acquiring all members of one class inside another class
2. It is a relationship between a parent class and child class
    i. A paraent class can also be called super or base class
    ii. While a child class can be called drive or suclass class

Types of Inheritance
----------------------

1. Single Inheritance 
   -------------------
    Class A (Parent) <---- Class B (Child)

    Single inheritance
    This is acquiring all members of one class inside another class
    P ==> C
E.g
'''
# # creating 2 classes for both parent (p) and child (C)
class P:
    def m1(self):
        print("Parent method from Single Inheritance")

class C(P):
    def m2(self):
        print("Child method")

c = C()
c.m1()
c.m2()
'''
Output is 
Parent method Single Inheritance
Child method
'''
# -------------------------------------------------------------
'''
2. Multilevel Inheritance 
    Class A (Grand-Parent) <----- Class B (Parent) <---- Class C (Child)

    Is the concept of inheriting the memebers from multiple classes to single class with the concept of one after another known 
    as multilevel inheritance
E.g
'''
# # creating 3 classes for grandparent (G) parent (P) and child (C)
class G:
    def m1(self):
        print("GrandParent method from Multilevel Inheritance")

class P(G):
    def m2(self):
        print("Parent method")

class C(P):
    def m3(self):
        print("Child method")

c = C()
c.m1()
c.m2()
c.m3()
'''
Output is 
GrandParent method from Multilevel Inheritance
Parent method
Child method
'''
# -------------------------------------------------------------
'''
3. Hierarchical Inheritance 
                     <---- Class A (Child)
    Class A (Parent) <---- Class B (Child)
                     <---- Class C (Child)

    It's the concept of inheritance members from one class into multiple classes which are present at same level is known 
    as Hierarchical Inheritance 
E.g
'''
# creating 3 classes for parent (P), Child 1 (C1), Child 2 (C2) and child 3 (C3)
class P:
    def m1(self):
        print("Parent method from Hierarchical Inheritance")

class C1(P):
    def m2(self):
        print("Child 1 method")

class C2(P):
    def m3(self):
        print("Child 2 method")

class C3(P):
    def m4(self):
        print("Child 3 method")

C1 = C1()
C2 = C2()
C3 = C3()
C1.m1()
C1.m2()
C2.m1()
C2.m3()
C3.m1()
C3.m4()
'''
Output is 
Parent method from Hierarchical Inheritance
Child 1 method
Parent method from Hierarchical Inheritance
Child 2 method
Parent method from Hierarchical Inheritance
Child 3 method
'''
# -------------------------------------------------------------
'''
4. Multiple Inheritance 
    Class A (Parent)
                       \
                         <---- Class C (Child)
                        /
    Class B (Parent)

    This is the concept of inheriting the members from multiple classes into a single class at a time is known 
    as Multiple Inheritance
E.g
'''
# creating 3 classes for parent 1 (P1), Parent 2 (P2) and child (C)
class P1:
    def m1(self):
        print("Parent 1 method from Multiple Inheritance")

class P2:
    def m2(self):
        print("Parent 2 method")

class C(P1,P2):
    def m3(self):
        print("Child method")

C = C()
C.m1()
C.m2()
C.m3()
'''
Output is 
Parent 1 method Multiple Inheritance
Parent 2 method
Child method
'''
# -------------------------------------------------------------
'''
5. Hybrid Inheritance 
   -------------------
              Class A (Grand-Parent)
                    /       \
    Class B (Parent)        Class C (Parent)
                    \       /
                 Class D (Child)
    This concept is the combination of the Single, Multi level, Multiple and Hierarchial Inheritances
E.g 1              
'''
# creating 4 classes for grandparent, parent 1 (P1), Parent 2 (P2) and child (C)
class G():
    def m1(self):
        print("GrandParent method from Hybrid Inheritance")

class P1:
    def m2(self):
        print("Parent 1 method")

class P2:
    def m3(self):
        print("Parent 2 method")

class C(G,P1,P2):
    def m4(self):
        print("Child  method")

C = C()
C.m1()
C.m2()
C.m3()
C.m4()
'''
Output is
GrandParent method from Hybrid Inheritance
Parent 1 method
Parent 2 method
Child  method
'''

# E.g 2
class Mercedes:
    def start(self):
        print("This is Mercedes Benz")

class AClass(Mercedes): 
    def model1(self):
        print("This is A Class Mercedes Benz")

class BClass(Mercedes):
    def model2(self):
        print("This is B Class Mercedes Benz")
    
class GWagon(AClass,BClass):
    def classic(self):
        print("GWagon is a classic and the most expensive Mercedes Benz")

GWagon = GWagon()
GWagon.start()
GWagon.model1()
GWagon.model2()
GWagon.classic()

'''
Output is
This is Mercedes Benz
This is A Class Mercedes Benz
This is B Class Mercedes Benz
GWagon is a classic and the most expensive Mercedes Benz
'''

# E.g 3
class Vehicle:
    def start(self):
        print("vehicle started")

class Car(Vehicle): # SINGLE INHERITANCE
    def drive(self):
        print("Car is driving")

class Bike(Vehicle): # HIERARCHICAL INHERITANCE
    def ride(self):
        print("Bike is riding")

class FlyingCar(Car,Bike): # MULTIPLE AND MULTILEVEL INHERITANCES
    def fly(self):
        print("Flying Car is flying")

flying_car = FlyingCar()
flying_car.drive()
flying_car.fly()
flying_car.ride()
flying_car.start()
'''
Output is
Car is driving
Flying Car is flying
Bike is riding
vehicle started
'''
# -------------------------------------------------------------
'''
Diamond Problem
----------------
This is if the same method is inherited from both parent classes (Multiple Inheritance), it creates ambiguity about which method
the child class should use then Python will always consider the order (MRO - Method Resolution Order) of Parent classes in the 
declaration of the child
E.g 
class P1:
    def m1(self):
        print("Parent 1 method")

class P2:
    def m2(self):
        print("Parent 2 method")

class C(P2,P1): # A child not knowing which method to call first can be confusing
    def m3(self):
        print("Child method")
'''
# -------------------------------------------------------------
'''
6. Cyclic Inheritance
   -------------------
i. This is the concept of inheriting members between the same class or from another class in a cyclic manner is called Cyclic 
or Circular Inheritance.
ii. In Cyclic or Circular Inheritance the child and parent roles becomes ambiguous which would result in undefined class names.
iii. Hence Python doesn't support Cyclic or Circular Inheritance.
E.g 
class A(A) i.e. A can't be a parent and also be a child
E.g
'''
class A(A):
    pass
class A(B):
    pass
class B(A):
    pass

'''
Output is
Traceback (most recent call last):
  File "/Users/olakoya/Desktop/automationwithpython/Day25/Inheritance_2.py", line 286, in <module>
    class A(A):
            ^
NameError: name 'A' is not defined
'''