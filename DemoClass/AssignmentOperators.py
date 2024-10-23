# Operator | Name | Example | Equivalent
# 1. += | Addition Assignement | i += 8 | i = i + 8
# 2. -= | Subtraction Assignement | i -= 8 | i = i - 8
# 3. *= | Multiplication Assignement | i *= 8 | i = i * 8
# 4. /= | Float Division Assignement | i /= 8 | i = i / 8
# 5. //= | Integer Division Assignement | i //= 8 | i = i // 8
# 6. %= | Remainder Assignement | i %= 8 | i = i % 8
# 7. **= | AExponent Assignement | i **= 8 | i = i ** 8

# Assignment operator is use to assign value to the variable e.g. x = 10
# We can combine assignment oeprator with some other operator to form compound assignemnt operator 
# E.g. x =+10 is the same thing as x = x+10

x,y = 10,20
x+=20 # x = x+20 = 30
y-=10 # y = y-10 = 10

print(x)
print(y)