""" Create a equilateral triangle patterns"""
n = 5
for i in range(5):
    print((" " * (n-1)) + ("*" * i) + ("*" * (i -1)))
    n -=1