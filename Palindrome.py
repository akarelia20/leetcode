def palindrome(x):
    if x < 0:
        return False
    y = x
    result = 0
    while y > 0:
        z= y %10
        y = y//10
        result = (result*10) + z
        
    if x == result:
        return True
    else:
        return False

print(palindrome(121))