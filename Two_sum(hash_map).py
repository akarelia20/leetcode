# Runtime: 80 ms, faster than 73.99% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 24.21% of Python3 online submissions for Two Sum.
#TIME_complexity:O(n) 
# SPACE_COMPLEXITY: O(n)

# leetcode link: https://leetcode.com/problems/two-sum/

###############################################################

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example :

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,3], target = 6
# Output: [0,1]
#################################################################################


def two_sums(nums, target):
    hash_map={}
    for i in range(0,len(nums)):
        res= target-nums[i]
        if res in hash_map:
            return hash_map[res],i
        hash_map[nums[i]]= i

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return two_sums(nums,target)