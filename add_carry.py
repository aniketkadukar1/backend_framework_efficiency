# Add -> 9 + 8 = 17 -> add -> 7 carry -> 1
# carry > add // 10 and add > add % 10 
num1 = [2, 4, 6, 8]
num2 = [8, 9, 7, 9]
carry = 0
output = []
for i in range(len(num1)-1, -1, -1):
    add = num1[i] + num2[i] + carry
    if add > 9:
        carry = add // 10
        add = add % 10
        output.append(add)

    else:
        carry = 0
        output.append(add)
output.append(carry)
print(output)
