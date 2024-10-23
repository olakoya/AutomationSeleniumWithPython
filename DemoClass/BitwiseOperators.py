# Bitwise Operators
# If we operate an oeprator bit by bit it's called Bitwise Operators
# These operators are applicable for int and boolean types only. 
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