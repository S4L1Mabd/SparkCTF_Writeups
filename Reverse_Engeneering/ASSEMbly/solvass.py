from pwn import *

# Constants
value = 5934314573
xor_value = 5

# XOR operation
result = value ^ xor_value 

print(result)

# Shift left by 3 bits
result >>= 3


print("Result after XOR and left shift:", result)

