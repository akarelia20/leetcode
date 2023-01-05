class Solution:
    def reverse(self, x: int) -> int:
        result= 0
        sign= -1
        if x < 0:
            x= x*-1
        else: 
            sign = 1
        while x > 0:
            result = (result*10) +(x%10)
            x = x//10
    
        return 0 if result > 2**31 else result*sign
            
            