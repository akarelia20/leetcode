class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        result = []
        
        for i in range(len(nums)):
            if i == 0:
                result.append(x)
            else:
                result.append(result[i-1] * nums[i-1]) 
        
        
        for j in range(len(nums)-1,-1,-1):
                result[j]= result[j]*x
                x = x*nums[j]
           
        return (result)
       
        