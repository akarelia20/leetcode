class Solution:
    def reverse(self, x: int) -> int:
        result= 0
        y= 0
        sign= -1
        if x < 0:
            x= x*-1
            print(x)
        else: 
            sign = 1
        while x > 0:
            y = x%10
            result = (result*10) +y
            print(result)
            x = x//10
            print("x", x)
    
        return 0 if result > 2**31 else result*sign
            
            