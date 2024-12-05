'''
3. Overriding Philosophy (methods, constructor)
------------------------------------------------
This is one of the important types of Polymorphism.

Overriding is supported for both Methods and Constructors.

In a class we have variable, method and constructors.

What is overriding?
In a parent class we create a chain of child's class. Whatever method we desrcibed in parent class if not satisfied can be recreated in child's class

Types of Overriding
--------------------
1. Method Overriding 
2. Constructor Overriding


    1. Method Overriding
    ---------------------
    Whatever members available in the parent class are available to child class by default.
    Through inheritance a child can acess a parent class.
    And if a child class isn't satisfied with parent class implementation then the child class is allowed ot redefine parent 
    class members based on business requirements is called Method Overiding.
E.g
'''
class RBUK:
    def rateofinterest(self):
        return 0

class Lloyds(RBUK):
    def rateofinterest(self):
        return 10

class HSBC(RBUK):
    def rateofinterest(self):
        return 12
'''
No output because there weren't an execution due to not having a parameter and without parameter there's no arguement
and for that reasons an object or object reference variable wasn't created.
'''
#----------------------------------------------

'''
    2. Constructor Overriding
    --------------------------
    As that of Method Overriding if a Constructor is redefined in a class as for the business requirements
E.g
'''
class P: # Parent class
    def __init__(self):
        print("Parent Constructor")

class C(P): # Child class
    def __init__(self,a): # constructor with a simple arguement 'a'
        super ().__init__() # And to use the parent method inside child class 'super' method is used
        print("Child Constructor")

c = C(10) # creating an object C() and passing value '10' to the parameter to 'a' in child class
'''
Output is 
Child Constructor

After adding line 56 Output becomes 
Parent Constructor
Child Constructor

E.g 2 from real life Scenario
'''
class Employee:
    def __init__(self, name, employee_id): # Employee constructor has name and employee_id
        self.name = name 
        self.employee_id = employee_id 

    def display_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}"
    
class Manager(Employee): # 'Manager' is also an employee but belongs to another 'department' as seen in the method below
    def __init__(self, name, employee_id, department): # Manager has an additional 'department' parameter in constructor
        super().__init__(name, employee_id) # Call parent constructor with only the required arguments
        self.department = department # Initialise the 'department' attribute in the Manager class

    def display_details(self):
        return f"{super().display_details()}, Department: {self.department}"

# Both Manager and Developer inherited method from Parent 'Employee' class
# And because the chain constructor in the parent isn't staifisying the child 1 and child 2 have created their own constructors

class Developer(Employee): # 'Developer' is an employee with the knowledge of 'programming_language'
    def __init__(self, name, employee_id, programming_language): # Developer has an additional 'programming_language' parameter
        super().__init__(name, employee_id) # Call parent constructor
        self.programming_language = programming_language # Initialise the 'programming_language' attribute

    def display_details(self):
        return f"{super().display_details()}, Programming_Language: {self.programming_language}"

# Creating a list of employees (Managers and Developers)
employees = [
    Manager( "Alice", 101, "HR"),           # Manager with department 'HR'
    Developer("Bob", 102, "Python")         # Developer with programming_language 'Python'
]

# Display details for all employees
for employee in employees:
    print(employee.display_details())

'''
Expected Output is 
Name: Alice, ID: 101, Department: HR
Name: Bob, ID: 102, Programming_Language: Python
'''
    
