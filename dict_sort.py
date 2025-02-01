dict1 = {123:"Aniket", 83:"Om", 73:"Bhau", 23:"Aai"}

d = dict(sorted(dict1.items(), key= lambda item : item[0], reverse=True))
print(d)