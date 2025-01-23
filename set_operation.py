a = [1, 3, 5, 6, 2, 5, 7, 8, 2, 7, 8 ,9]
b = [1, 5, 7, 3, 5, 7, 5 ,2, 3]

print(set(a) | set(b)) # Union 
print(set(a) & set(b)) # Intersection
print(set(a) - set(b)) # difference