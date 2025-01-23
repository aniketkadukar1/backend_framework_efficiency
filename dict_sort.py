dict1 = {123:"Aniket", 83:"Om", 73:"Bhau", 23:"Aai"}

d = sorted(dict1.keys())
temp ={}
for i in d:
    temp[i] = dict1[i]

print(temp)