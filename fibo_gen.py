def gen(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b
        

g = gen(10)

print(next(g))
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
