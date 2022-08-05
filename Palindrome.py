#  check if the number is palindrome.
#  this slution only itrates through have of the length of the given number.


def palindrome(x):
    if x < 0 or (x >0 and x%10 == 0):
        return False
    result = 0
    while result < x:
        result = (result*10) + x%10
        x = x//10
        print(x)
        print(result)
    if (x == result or x == result//10):
        return True
    else:
        return False
print(palindrome(10))