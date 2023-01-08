class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos= 0
        
        for i in nums:
            if i !=0:
                nums[pos]= i
                pos+=1
        
        for j in range(len(nums)-1,pos-1,-1): 
            nums[j] = 0
        
        return nums
                
        