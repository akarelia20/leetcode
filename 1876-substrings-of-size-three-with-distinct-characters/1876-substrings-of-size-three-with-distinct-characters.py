class Solution:
    from collections import deque
    def countGoodSubstrings(self, s: str) -> int:
        count= 0
        queue = deque(list(s))
        
        while len(queue) >= 3:
            left = queue.popleft()
            middle = queue[0]
            right = queue[1]
            
            if left != right and right != middle and left!= middle:
                count+=1
        return count
                
        