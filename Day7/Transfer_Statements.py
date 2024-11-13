'''
Transfer statements or Jumping Statements
-----------------------------------------
Types of Statements are
1. Break
    We can use break statement inside loops to break (while or for) loop execution based on some condition.
2. Continue
    We can use continue statement inside loops to skip loop execution based on some condition.
3. Pass 
    Pass is a keyword in Python.
    In our programming syntactically if block is required which won't do anything then we can 
    define the empty block with pass keyword
    To create an empty set "paa" statement is used
'''
# break range (start, stop) value
# for x in range(1,10): # start count from 1 and stop at 10
#     print(x)
'''
Output is
1
2
3
4
5
6
7
8
9
'''
# for x in range(1,10): 
#     if x == 5:
#         break
#     print(x)
'''
Output is
1
2
3
4
As you can see from above output that the count breaks on getting to 5 based on the code
'''

# continue
# for x in range(1,10): 
#     if x == 5:
#         continue
#     print(x)
'''
Output is
1
2
3
4
6
7
8
9
As you can see from above output that 5 is ommitted based on the code
'''

# pass
# for x in range(1,10): 
#     if x == 5:
#         pass
#     print(x)
'''
Output is
1
2
3
4
5
6
7
8
9
Pass does nothing in the statement
'''

# pass
# for x in range(100): 
#     if x%9 == 0: # divisible by 9
#         print(x)
# else:
#     pass
'''
Output is
0
9
18
27
36
45
54
63
72
81
90
99
'''
for x in range(100): 
    if x%9 == 0: # divisible by 9
        if x%2 == 0:
            print(x)
            break # the execution is terminated at this stage by breaking it and then the rest of the code below isn't executed
        print(x) # this is to comment out
else:
    pass
'''
Output is 
0
Inside loop execution, if break statement not executed, then only else part will be executed.
"else" means loop without break.
'''
'''
Before break or continue ==> statements will be executed.
After break, statements will not be executed including else book in the for loop as seen in the above code.
After continue, else block will be executed in the for loop.
"Provided condition" is statisfied for both break and continue.

We can use loops for repeat code executuion.
Repeat code for every item in sequence for loop.
Repeat code as long as condition is true while loop.
'''