class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_num= set()
        for num in nums:
            if num in unique_num:
                return True
            else:
                unique_num.add(num)
        return False
                
                