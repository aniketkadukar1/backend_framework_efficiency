def get_intersection(l1, l2):
    return list(set(l1) & set(l2))

l1 = [x for x in input().split()]
l2 = [x for x in input().split()]
print(get_intersection(l1, l2))