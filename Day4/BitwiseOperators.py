# Bitwise Operators
# If we operate an operator bit by bit it's called Bitwise Operators
# These operators are applicable for integer and boolean types only. 
# For any other data types we will get error ie strings or float etc will give error

# Operator | Name | Example | Result
# 1. & | Bitwise AND | 6 & 3 | 2
# 2. | | Bitwise OR | 10 | 10 |10
# 3. ^ | Bitwise XOR | 2^2 | 0
# 4. ~ | Bitwise 1's complement | ~9 | -10
# 5. << | Left-Shift | 10<<2 | 40
# 6. >> | Right-Shift | 10>>2 | 2

a = 10 # binary: 1010
b = 4 # binary: 0100
print(f"Bitwise AND (a & b): {a & b}") # Result: 0 (binary: 0000)
print(f"Bitwise OR (a | b): {a | b}") # Result: 14 (binary: 1110)
print(f"Bitwise XOR (a ^ b): {a ^ b}") # Result: 14 (binary: 1110)
print(f"Bitwise NOT (a ~ b): {~a}") # Result: -11 (binary: ~1010 = 0101 => -11 in two's complement)
print(f"Left Shift (a << 1): {a << 1}") # Result: 20 (binary: 10100)
print(f"Left Shift (a >> 1): {a >> 1}") # Result: 5 (binary: 0101)
'''
Output
Bitwise AND (a & b): 0
Bitwise OR (a | b): 14
Bitwise XOR (a ^ b): 14
Bitwise NOT (a ~ b): -11
Left Shift (a << 1): 20
Left Shift (a >> 1): 5
'''
"""
In binary 
2^3 = 8
2^2 = 4
2^1 = 2
2^0 = 1
Therefore,
10 in binary of 8 4 2 1 is 1010
4 in nibary of 8 4 2 1 is 0100

AND in binary of 8 4 2 1 is 0000 equals 0
OR in binary of 8 4 2 1 is 1110 equals 14 i.e 8+4+2 = 14
XOR in binary of 8 4 2 1 is 1110 equals 14 i.e 8+4+2 = 14
~10 in binary of 8 4 2 1 is 1011 equals 11 i.e 8+2+1 = 11
<<1 in binary of 8 4 2 1 is 1011 equals 11 i.e 8+2+1 = 20

~10 is nothing but a bitwise compliment
If a number is a negative number it's always represented by 2's compliment form
2's complemt is represented by 1's compliment+1
1's complement
E.g
If we have 1 --> 0
If we have 0 --> 1

        MSB                        LSB
10      0   0   0   0   1   0   1   0
~10     1   1   1   1   0   1   0   1

            1   1   1   0   1   0   1
  1'SC      0   0   0   1   0   1   0
        1                           1
            0   0   0   1   0   1   1   
<<1     0   0   0   1   0   1   0   0
>>2     0   0   0   0   0   0   1   0     

The most significant bit acts as sign bit. 0 value represents +ve number while 1 represent -ve number
+ve numbers will be represented directly in the memory where as -ve numbers will be represented indirectly in 2's complemet form

P - PARENTHESIS - ()
E - EXPONENTS - **
D - DIVISION - /
M - MULTIPLICATION - *
A - ADDITION - +
S - SUBTRACTION - -
"""