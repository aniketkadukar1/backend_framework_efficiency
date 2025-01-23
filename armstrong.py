# Armstrong num
# 153
# 3  --> 153 % 10
# 15 --> 150 //10
# res += mod ** len(num)

def armstrong_num(num):
    temp = num
    length = len(str(num))
    result = 0
    while num:
        result += (num % 10) ** length
        num = num // 10
    if temp == result:
        return True
    return False

print(armstrong_num(9474))