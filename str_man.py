str = "The sky is blue"

str_list = str.split()
str2  = []
for i in range(1,len(str_list)+1):
    str2.append(str_list[-i])


print(" ".join(str2))