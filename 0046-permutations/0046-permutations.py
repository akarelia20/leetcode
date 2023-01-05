class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        result=[]

        def helper(first):
            if first == n:
                return result.append(nums[:])
            for i in range(first,n):
                # swapping
                nums[first], nums[i] = nums[i],nums[first]
                helper(first+1)
                # unswapping
                nums[first], nums[i] = nums[i],nums[first]              

        helper(0)
        return result