# Iterables gives one value at a time (Lazy Loading)
# Iterables is an object that can be iterate over.
# Iterables example --> list, tuple, string, dictonaries and set
# Iterator --> Iterable is a function to which iterable can be passed. and it gives element one by one.
# We need to pass iterable to an iterator object. and to get one value at a time we need to use next() function.

nums = [1, 3, 5, 7, 3, 6, 2]



it = iter(nums)

print(next(it))
print(next(it))
print(next(it))
