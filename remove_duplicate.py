# abdndai
# aabddin
def remove_duplicate(l1):
    l1.sort()
    l = 0
    r = 1
    while l < len(l1):
        if l1[l] == l1[r]:
            del l1[r]
        else:
            l+=1
            r+=1
    return l1

print(remove_duplicate([2, 3, 7, 4, 2, 1, 6, 8, 5, 7, 4]))

