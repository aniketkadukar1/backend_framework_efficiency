def gen(num):
    series = [0, 1]
    for i in range(num - 2):
        series.append(series[-1] + series[-2])
    return series

print(gen(10))