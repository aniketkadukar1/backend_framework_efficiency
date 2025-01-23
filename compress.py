s = 'aaaabbbccccdddddee'
# new_s = ''
# count = 1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         count += 1
#     else:
#         new_s = new_s + s[i] + str(count)
#         count = 1
# new_s = new_s + s[-1] + str(count)

# print(new_s)

def compress(s):
    new_s = ''
    counter = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            counter += 1
        else:
            new_s += s[i] + str(counter)
            counter = 1
    new_s += s[i] + str(counter)
    return new_s

print(compress(s))
