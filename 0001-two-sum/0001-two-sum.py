class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {}
        for i in range(len(nums)):
            num2= target - nums[i]
            if num2 in visited_nums:
                return [i, visited_nums[num2]]
            else:
                visited_nums[nums[i]] = i
                
                