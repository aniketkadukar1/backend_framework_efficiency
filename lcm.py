# LCM : 12 , 18 ==> 36

# def check_lcm(a, b):
#     lcm = max(a, b)
#     while True:
#         if lcm % a == 0 and lcm % b == 0:
#             return lcm
#         lcm += 1

# print(check_lcm()) 

def find_lcm(a, b):
    lcm = max(a, b)
    while True:
        if lcm%a == 0 and lcm%b ==0:
            return lcm
        lcm += 1

print(find_lcm(10, 12))
