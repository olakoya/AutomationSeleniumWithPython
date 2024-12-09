'''
Interface
----------
Abstract Class contains ==> Fully Implented Method + Partially Implemented Method ==> LINE 31
Interface means ==> Only Unimpleneted Methods ==> LINE 19
If a Class contains only Abstract Methods are called ==> Interface e.g Selenium Webdriver User Interface
With the help of Selenium Wedrvier one would executes different automation on web browsers
Each and every browser is like a ==> Child Class
And Child Class consists of fully implemented ==> Parent Child Abstract Methods
Therefore, Selenium Webdriver is an ==> Interface
An example of Interfcace is ==> Selenium Webdriver
To start interface everything has to be imported from ==> ABC Module
To have access to everything available in ABC Module one needs to use ==> a star * when importing
E.g ==> "from abc import *"
E.g
'''
from abc import *

class DBInterface(ABC): # this class is an INTERFACE CLASS but must be inherited from ABC class vice versa
    @abstractmethod
    def connect (self): # defining a method
        pass

    @abstractmethod
    def disconnect(self):
        pass

# the above class is a parent class while the below class is a child class
# And the parent class "DBInterface" is fully implemented in the child class

class SqlServer(DBInterface): # ABSTRACT CLASS who is a child class with an unimplemented method in line 36
    def connect(self):
        print("Connecting to Oracle Database")

    @abstractmethod
    def disconnect(self): # unimplemented method
            pass

class Oracle(DBInterface): # CONCRETE CLASS who is a class class and fully implemented
    def connect(self):
        print("Connecting to Oracle Database")

    def disconnect(self):
        print("Disconnecting to Oracle Database")

class Sybase(DBInterface):
    def connect(self):
        print("Connecting to Sybase Database")

    def disconnect(self):
        print("Disconnecting to Sybase Database")

'''
Concrete Class
---------------
Concrete Class means ==> Only Fully Implemented Methods ==> LINE 39
i. If you don't know anything about implementation but just have requirement specification then we should go for interface.
ii. If we are talking about implementation but not completely, then we should go for abstract class i.e (pertially implemented class)
iii. If we are talking about implementation completely and ready to provide service then we should go for concrete class.
'''