'''
Dictionary Data Structure
--------------------------
DDS comprises of List(), Tuple{} and Set[]
- These are the group of individual objects as a single entity
- Dictionary is a group of objects as key-value pairs e.g
    1. RollNos ==> Name is Key
    2. PhoneAddress ==> Address is Value
    3. IpAddress ==> Domain Name
Dictionary ==> {key1:value1, key2:value2, key3:value3}
- Duplicate keys are not allowed but value values can be duplicated
- Heterogenous object (belongs to different datatype) are allowed ==> keys and values
- Insertion order is not preserved
- Dictionaries are mutable (i.e. update data), dynamic (i.e. change the size)
- Index and slicing is not possible

Dictionary in Java is called ==> Map
While in Python it's called ==> Hash

E.g
'''

# Create a Dictionary - Empty callibrace {} is called a dictionary data structure
# d = {} # dictionary data structure
# print(type(d))
'''
Output is
<class 'dict'>
'''

# d1 = dict() # type casting function
# print(type(d1))
'''
Output is
<class 'dict'>
'''

# Adding Entries inside empty Dictionary
# d = dict()
# print(d)
# d[100] = 'ram'
# d[200] = 'ravi'
# d[300] = 'shiva'
# print(d)
# print(type(d))
'''
Output is
{100: 'ram', 200: 'ravi', 300: 'shiva'}
<class 'dict'>
'''

'''
- When a data is added into a dictionary, the dictionary will first of all check whether that key is available or not
- If the key is available old value is replaced by new value
- Otherwise New entry is created in dictionary when no entry with that key is available
E.g
'''

# Elements in Advance
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
# print(d)
# print(type(d))
'''
Output is
{100: 'ram', 200: 'ravi', 300: 'shiva'}
<class 'dict'>
'''

'''
- We can access data inside dictionary by using keys
E.g
'''

# Access Elements inside Dictionary
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
# print(d[100])
# print(d[300])
# print(d[500]) # KeyError
'''
Output is
ram
shiva
print(d[500])
KeyError: 500
'''

'''
- If key is not available output will be KeyError
- Membership Operators presence is use to check ==> in and not in membership
E.g
'''
# After commenting line 78
# if 500 in d:
#     print(d[500])
'''
Output is
ram
shiva
'''
# Update Data inside Dictionary
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
# print(d)
# d [400] = "John"
# d [100] = "Johnny"
# print(d)
'''
Output is 
{100: 'ram', 200: 'ravi', 300: 'shiva'} ==> Dictionary before Update
{100: 'Johnny', 200: 'ravi', 300: 'shiva', 400: 'John'} ==> Dictionary after Update
'''

'''
- Delete is represented by ==> del in Dictionary
        del d[key]
E.g
'''

# Delete Data inside Dictionary
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
# print(d)
# del d[300]
# print(d)
'''
Output is
{100: 'ram', 200: 'ravi', 300: 'shiva'} ==> Dictionary before Delete
{100: 'ram', 200: 'ravi'} ==> Dictionary after Delete
'''

# Clear Data
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
# print(d)
# d.clear() # this is only clearing the data but not deleting the whole of the data
# print(d)
'''
Output is
{100: 'ram', 200: 'ravi', 300: 'shiva'} ==> Dictionary before Clearing
{} ==> Dictionary after Clearing
'''

'''
- Unbinding Operations that is there wouldn't be ab=ny access again after deletion
E.g
'''

# Delete Data
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
# print(d)
# # del d # one needs to doublecheck before deleting
# del d[500] # KeyError
# print(d)
'''
Output is
NameError: name 'd' is not defined
{100: 'ram', 200: 'ravi', 300: 'shiva'} ==> this means d doesn't exist in dictionary


Output after adding line 149
    del d[500]
KeyError: 500
'''

# Functions on Dictionary
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
# print(len(d))
# print(d[100])
# print(d.get(100))
# print(d.get(100, "Shyla"))
# print(d.get(500, "Shyla"))

'''
Output is
3
ram
ram
ram
Shyla ==> returned Default Value because 500 doesnt exist in dictionary
'''

# Using Pop Method: This will remove specific entry
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
# print(d)
# print(len(d))
# print(d.pop(100))
# print(d)
'''
Output is
{100: 'ram', 200: 'ravi', 300: 'shiva'}
3
ram
{200: 'ravi', 300: 'shiva'}
'''

# PopItem: This is a method that will remove all arbitary item from dictionary and return it
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
# print(d)
# print(len(d))
# print(d.pop(100)) # removes
# print(d.popitem()) # removes and return last item in the dictionary
# print(d)
'''
Output is
{100: 'ram', 200: 'ravi', 300: 'shiva'}
3
ram
(300, 'shiva')
{200: 'ravi'}
'''

d = {100: 'ram', 200: 'ravi', 300: 'shiva'}
print(d)
# print(d.keys()) # accessing only keys
# print(d.values()) # only values
# print(d.items()) # only items
# print(d)
'''
Output is
{100: 'ram', 200: 'ravi', 300: 'shiva'}
dict_keys([100, 200, 300])
dict_values(['ram', 'ravi', 'shiva'])
dict_items([(100, 'ram'), (200, 'ravi'), (300, 'shiva')])
{100: 'ram', 200: 'ravi', 300: 'shiva'}
'''

d1 = d.copy()
print(d1)
'''
Output is
{100: 'ram', 200: 'ravi', 300: 'shiva'}
{100: 'ram', 200: 'ravi', 300: 'shiva'}
'''