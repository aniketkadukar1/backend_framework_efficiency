def is_perfect_num(num):
    res = 0
    for i in range(1, num):
        if num % i == 0:
            res += i
    if res == num :
        print("Perfect Num")
    else:
        print("not perfect number")
    print(res)

is_perfect_num(496)