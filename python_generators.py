def generate_top_ten():
    n = 1
    while n <= 10:
        yield n
        n += 1

val = generate_top_ten()

for i in val:
    print(i)


# Python maps
nums = list(range(1, 11))
print(nums)
sq_num = list(map(lambda x : x ** 2, nums))
print(sq_num)

# Python filter
filter_even = list(filter(lambda x : x % 2 == 0, nums))
print(filter_even)

# Python Reduce 

from functools import reduce

addition = reduce(lambda x, y : x + y, nums)
print(addition)