class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n!= 1:
            if n in visited:
                return False
            visited.add(n)
            
            result = 0
            for i in str(n):
                result += int(i)**2
            n= result
        
        return True