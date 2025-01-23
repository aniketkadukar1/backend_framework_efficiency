list1 = [2, 4, 7, 2, 1, 4, 5, 7, 9, 7, 2, 3]
sum = 6
for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] + list1[j] == sum:
            print(list1[i], list1[j])
