'''
Counting Substring in the given String
--------------------------------------
If substring is present and want to get index question one will go for find
And when we want to count in the substring irt will count by searching beginning and ending in the substring in the index

Two Parameters to search in the String
----------------------------------------
1. Count ==> is the search for substring in the beginning of the main string
2. Count starts from (substring, begin, end) this will start number of occurrence of a string i.e. how many times of a
    substring in the main string
E.g
'''
s = "Donald Trump Donald"
sub = 'a'
sub = 'Donald'# sub is substring
# i.e. knowing how many times 'a' is present in the main string "Donald Trump"
print(s.count(sub)) # to see an output 'print' statement is used and added in 's.count(sub)
'''
Output is 
1

Adding another "Donald" to line 14 and running the code again
Output is 
2

Also adding line 16 and the output is still 
2
because there are 2 'Donald's and 2 'a's
'''

'''
HOMEWORK
--------

Write a code to check the beginning and ending in a substring from main string
'''

def check_start_end(main_string, substring):
    # Check if the main string starts with the substring
    starts_with = main_string.startswith(substring)

    # Check if the main string ends with the substring
    ends_with = main_string.endswith(substring)

    return starts_with, ends_with

# Example usage
main_string = "hello world"
substring = "hello"

starts, ends = check_start_end(main_string, substring)
print(f"Starts with '{substring}': {starts}")
print(f"Ends with '{substring}': {ends}")

'''
Output is
Starts with 'hello': True
Ends with 'hello': False
'''
