def get_num_vowels(s1):
    v = 'aeiouAEIOU'
    result = 0
    for i in range(len(s1)):
        if s1[i] in v:
            result += 1
    return result

print(get_num_vowels("aeioubcd"))
