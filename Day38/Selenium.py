'''
Introduction to Selenium WebDriver
-----------------------------------
Selenium contains a Suite and this suite contains component
Selenium is a single tool

Selenium Suite Components
---------------------------
    i. Selenium IDE ==> This is a browser extension and can be called record anf playback tool
    ii. Selenium WebDriver ==> This is the most important tool and has a combination of tools. It's used for automation purpose and
     interact with browser with the help of programming language. And this is most important, popular and powerful tool
    iii. Selenium RC ==> It's combined with selenium IDE itself
    iv. Selenium Grid ==> This is used for parallel testing on multiple platforms and browser

Selenium is a package
WebDriver is a module
Module contains Functions and Classes

Package contains => Modules
Modules contains => Functions and Classes

Chrome Browser calls ==> Chrome class()
Edge Browser calls ==> Edge class()
Firefox Browser ==> Firefox class()

Selenium WebDriver is only used to automate GUI or web application
Selenium WebDriver cannot automate APIs and DeskTop Application
WebDriver is an programming interface and it's act like an API
Every web application in this modean world follows client - server architecture

3 Types of Layers
-----------------=
Presentation Layer
API Layer
Backend Layer

Setting Up and Installation
----------------------------
1. Python ==> A programming language
2. Pycharm ==> Clients Library
Selenium WebDriver ==> Automation tools

Below is steps to install Selenium WebDriver
i. Opening on Pycharm for new project
ii. Install Pip package name using terminal
        Pip list will show and check all packages installed 
iii. Pycharm project settings
        Go to pycharm and click on settings
        Click on Project: Selenium to expand it
        Then click on Python Interpreter
        Click on plus + signs to add or search for available Packages
        Type Selenium in the search box and click install package when selenium highlighted
        Then close and click ok in the interpreter window
iv. Requirements.txt file ==> pom.xml
        Right click on selenium folder
        Click on New
        and click on file
        Name your .txt file

Types of packages
------------------
selenium
pandas
matplotlib

In terminal type 'pip install -r requirements.txt'
Type pip list to verify installation
'''
#-----------------------------------------------------------
'''
First Test Cases Example
-------------------------
1. Open Web Browser (Chrome/Firefox/Edge)
2. Open URL https;//www.google.com/
3. Capture title of the page (Actual Title)
4. Verify title of the page: Google (Expected Title)
5. Close browser

Steps
-----
Go to pycharm
Right click on selenium and select New
Click on New and select Directory
Give the Directory a name
Right click on created Directory and click on New
On new, select python file
And then give it a name

'''