'''
Flow Control or Control Statements in Python
---------------------------------------------
A flow control decides orders in which statements need to be executed.
Only few statments can be executed in all statements.

Types of Statements
-------------------
1. Conditional Statements
2. Transfer Statements
3. Iterative Statements or 
4. Looping Statements

Conditional Statements (Examples are located in Day 5 Conditional_Statements.py file)
-----------------------
When we talk about Conditional Statement we need to specify some conditions, 
and that condition is either Logical or Expressions conditions

E.g of 
Logical Statements;
-------------------
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

There are different types of Conditional Statements and examples are;
1. if
2. if-else
3. if-elif-else
4. nested if-else

Based on some conditions you perform some actions and those actions are powerful statements
Logical conditions or expressions will return a boolean value when performed

if or simple if statement
-------------------------
if condition (is True): (you need to perform an action)
Action can be a statement
We can have multiple statements e.g statement 1, statement 2, statement 3 etc. and they are simply grouped together 
If an "if" condition is a True statement it will be executed inside the "if or simple if" statement otherwise it won't be executed
for every statement in python


if-else statement requires multiple actions
--------------------------------------------
if condition:
    Action-1
else:
    Action-2
'''

'''
To specify multiple conditions we go for;

if-elif-else statement
----------------------
if condition-1: is True
    Action-1 will be executed
else condition-2:
    Action-2 will be executed    
elif condition-3:
    Action-3 will be executed
else: 
    Default Action (i.e if the other first "if and else" statements are not true)

In Java we can switch statement but not in Python hence using the above "if" statements

'else' plug is always optional and based on 

'''
'''
nested if-else statement
-------------------------

else part is always optional hence, the following are various possible syntaxes
    if
    if-else
    if-elif-else
    if-elif
The above are 4 types of the if conditional statements.
There is no switch statement in Python
'''
'''
Iterative or Looping Statements
--------------------------------
If we want to execute some statements multiple times ie. looping or executing the statements multiple times
It could be either
1. while loop
2. for loop

while loop statements (Examples are located in Day 6 Interactive_Statements.py file)
----------------------
If will want to execute a group of statements in a loop until a condition is false

Syntax for using while loop is
    1. Initialiazation ==> start value
    2. Condition 
    3. Increment/Decrement
Without the above 3 it's impossible to execute loop statement
'''

'''
For Loop (Examples are located in Day 7 Range_Function.py file)
--------
Loop is a range of functions and it's a sequence of numbers.
Once you specify some values it will generates sequence of numbers by considering 'start' value and by not considering 'end' value
E.g
form - 1 ==> range(stop)
form - 2 ==> range(start,stop)
form - 3 ==> range(start,stop, step)

start and step parameters are always optional.
One can specify steps if it generates sequece of numbers.

Step value always decides the difference between 2 consecutive numbers
Default value of step is 1

Step ==> positive ==> forward direction ==> L to R ==> stops or end at - 1
Step ==> negative ==> reverse direction ==> R to L ==> stops or end at + 1

'''