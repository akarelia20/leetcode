class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter= 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[counter]= nums[i+1]
                counter+=1
        return counter