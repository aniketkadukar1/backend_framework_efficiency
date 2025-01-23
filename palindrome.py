str1 = "madam"

def is_palindrome(str1):
    l = 0
    r = len(str1) - 1
    while l < r:
        if str1[l] != str1[r]:
            return False
        l += 1
        r -= 1
    return True

print(is_palindrome(str1))
        
        
