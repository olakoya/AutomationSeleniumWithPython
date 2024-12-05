'''
Polymorphism
-------------
Poly ==> means Many
Morphs ==> means Forms

Which means Polymorphism means many more forms that's the same person but different personalities at different places
E.g
---
i. Student can be well behaved at home but different in school i.e having 2 personalities.
ii. many operators like;
    + ==> is an addition, and when applied on string it's called concatenation operator
    * ==> is a multiplication but when applied on string it becomes repetition concatenation operator

Types of Polymorphoses
----------------------
1. Duck Typing Philosophy
2. Overloading (variables, methods, constructor)
3. Overriding (variables, methods, constructor)
'''
#------------------------------------------------------
'''
1. Duck Typing Philosophy
--------------------------
This is defining a function and taking a object that is a parameter as written below;
        def f1(obj):
            print(obj) # obj means a variable that we can pass any types of value

Python is a Dynamically Typed of Programming Language which means one can't specify the datatype of any object based on 
the type of value but during the execution type we can provide the datatype i.e
    At runtime, if "it walks like a duck and talks like a duck, it must be a duck". 
Python follows this principle. This is called Duck Typing Philosophy or Python
    If i pass string value to the class, it must also be a string datatype during runtime likewiise integer too
E.g
'''
class Duck:
    def talk(self):
        print("Duck talks Quack...Quack")

class Dog:
    def talk(self):
        print(" Dog talks Bark...Bark")

class Cat:
    def talk(self):
        print("Cat talks Meow....Meow")

class Cow:
    def talk(self):
        print(" And Cow talks Mooon....Mooon")

# creating a function for the above class objects
def f1(obj):
    obj.talk() 

# for that reason we are using a list variable in respect to the objects of the class
I = [Duck(), Cat(), Dog(), Cow()]
for obj in I: # for loop for object in the above list call the the below functions object
    f1(obj)
'''
Output is
Duck talks Quack...Quack
Cat talks Meow....Meow
 Dog talks Bark...Bark
 And Cow talks Mooon....Mooon

Noticed in the output that ==> the execution didn't follow the arrangement of the class but only followed the list 'I' arrangement
'''

