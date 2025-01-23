def remove_element(l1, e_index):
    if e_index < 0 or e_index > len(l1):
        return "Index is not available"
    else:
        l1.pop(e_index)
        return l1
    
print(remove_element([2, 5, 7, 2, 6, 8, 3, 2, 5, 1 ,0], 3))