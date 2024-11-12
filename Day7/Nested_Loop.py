'''
NESTED LOOPS FUNCTION
----------------------
A loop inside another loop is called Nested Loop.
Sometimes we can take a loop inside another loop, which are alos knows as Nested Loops.
'''
for i in range (1,5): # outer loop # i - 1
    for j in range(1,6): # inner lloop # j - 1 2 3 4
        print(f"{i} * {j} = {i * j}", end="\t")
'''
Output is
1 * 1 = 1       1 * 2 = 2       1 * 3 = 3       1 * 4 = 4       1 * 5 = 5       2 * 1 = 2       2 * 2 = 4       2 * 3 = 6      
2 * 4 = 8  2 * 5 = 10       3 * 1 = 3       3 * 2 = 6       3 * 3 = 9       3 * 4 = 12      3 * 5 = 15      4 * 1 = 4       
4 * 2 = 8       4 * 3 = 12 4 * 4 = 16       4 * 5 = 20  
'''

'''
Transfer statements or Jumping Statements
-----------------------------------------
Types of Statements are
1. Break
    We can use break statement inside loops to break loop execution based on some condition.
2. Continue
    We can use continue statement inside loops to skip loop execution based on some condition.
3. Pass
    Pass is a keyword in Python.
    In our programming syntactically if block is required which won't do anything then we can 
    define the empty block with pass keyword
'''