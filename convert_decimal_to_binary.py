"""
--> 2^3 + 2^2 + 2^1 + 2^0
0 -> 0000
1 -> 0001
2 -> 0010
3 -> 0011
4 -> 0100
"""


def decimal_to_binary(num):
    binary = ''
    while num:
        mod = num % 2
        binary  = str(mod) + binary
        num = num // 2

    return binary

print(decimal_to_binary(16))