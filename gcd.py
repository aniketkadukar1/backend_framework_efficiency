def check_gcd(a, b):
    min_num = min(a, b)
    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return False

print(check_gcd(9, 30))