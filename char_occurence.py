s = "oihsaoidhasudboasu"
# char = 'h'
# count = 0
# for i in range(len(s1)):
#     if s1[i] == char:
#         count += 1
# print(count)

# ch = {}

# for i in range(len(s)):
#     if s[i] not in ch:
#         ch[s[i]] = 1
#     else:
#         ch[s[i]] += 1

# print(min(ch, key= ch.get))


ch = {}

for i in range(len(s)):
    if s[i] in ch:
        ch[s[i]] += 1
    else:
        ch[s[i]] = 0

print(ch)