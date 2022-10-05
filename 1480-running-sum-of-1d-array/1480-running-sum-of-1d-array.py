class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = []
        for i in range(0,len(nums)):
            if i == 0:
                sum.append(nums[i])
            else:
                sum.append(sum[i-1]+nums[i])
        return sum