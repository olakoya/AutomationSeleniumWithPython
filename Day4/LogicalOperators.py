# a-True, b-True, a and b-True, a or b-True, not a-False
# a-True, b-False, a and b-False, a or b-True, not a
# a-False, b-True, a and b-False, a or b-True, not a-True
# a-False, b-False, a and b-False, a or b-False, not a-

# For Boolean Data Type
#       and => If both arguements are True then it is True
#       or => If atleast one arguement is True then result is True
#       not (!=) => Complement is if one arguement is False it's False

# For Non Boolean Data Types
#       0 means False
#       non-zero means True
#       empty string is always treated as False

#  E.g x and y
# if x is 0 and y is 10 ans will be ==> 0
# if x is 0 or y is 10 ans will be ==> 10
# if x is 0 not y is 10 ans will be ==> 0

# x and y
print (0 and 10) # Output is 0 because 0 is False while 10 is True, so False and True = False (you pick the boolean that appears to be False)
print (10 and 20) # Output is 20 because 10 is True while 10 is True, so True and True = True (you pick the content/variable that comes last)
print (20 and 10) # Output is 10 because 20 is True while 10 is True, so True and True = True (you pick the content/variable that comes last)
print (10 and 0) # Output is 0 because 10 is True while 0 is False, so True and False = False (you pick the boolean that appears to be False)

# x or y
print (0 or 10) # Output is 10 because 0 is False while 10 is True, so False or True = True
print (10 or 20) # Output is 10 because True or True = True (you pick the first true which is 10)
print (20 or 10) # Output is 20 because True or True = True (you pick the first true which is 20)
print (10 or 0) # Output is 10 because 0 is False while 10 is True, so False or True = True

# x != y
print(0 != 10) # Output is True because 0 is not 10
print(10 != 20) # Output is True because 10 is not 20
print (20 != 10) # Output is True because 20 is not 10
print (10 != 0) # Output is True because 10 is not 10
print (20 != 20) # Output is False because 20 is 20

# not False ==> True
# not True ==> False