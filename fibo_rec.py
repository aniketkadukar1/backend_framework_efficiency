def fibo(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibo(num - 2) + fibo(num -1)
    
print(fibo(10))