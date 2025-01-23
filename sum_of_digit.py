# 9238

def sum_of_digit(num):
    result = 0
    while num > 0:
        digit = num % 10 # 8
        num = num // 10 # 923
        result = result + digit # Sum
    return result

print(sum_of_digit(129238103))