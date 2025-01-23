def str_format(s):
    temp_list = []
    s_list = s.split("_")

    for i in s_list:
        temp_list.append(i[0].lower()+i[1:].upper())
    
    s = ".".join(temp_list)
    print(s)


s = "This_Is_Aniket_K"
str_format(s)