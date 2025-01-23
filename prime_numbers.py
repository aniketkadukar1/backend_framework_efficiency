def is_prime_num(num):
    if num < 2:
        return False
    for i in range(2, num//2+1):
        if num%i == 0:
            return False
    return True

print(is_prime_num(2))
print(is_prime_num(10))
print(is_prime_num(7))
print(is_prime_num(9))
print(is_prime_num(17))