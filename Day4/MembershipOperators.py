# Membership Operators
# This means it will check presence of an element/object/item inside a sequences (string, list, tuple, set, dictionary) nlike multple sequences
# Types of Membership Operators are
# 1.   in ==> True, False (i.e. if an element is present it will return True Boolean Value and if not it will return False Boolean Value)
# 2.  not in ==> True, False (i.e. if an element is not present it will return either True Boolean Value and if not it will return False Boolean Valuee)

# Special Operators

a = "Welcome" # "Welcome" is a sequence in "a" Value, Capital "W" is an element or an item.
print("w" in a) # Output is a False Boolean Value because small letter "w" isn't part of the "Welcome" sequence
print("w" not in a) # Output is a True Boolean Value because small letter "w" isn't part of the "Welcome" sequence

print("W" in a) # Output is a True Boolean Value because small letter "w" isn't part of the "Welcome" sequence
print("W" not in a) # Output is a False Boolean Value because small letter "w" isn't part of the "Welcome" sequence

# Membership operators will always check the presence