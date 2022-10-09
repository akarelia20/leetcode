class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = set()
        for num in nums:
            if num not in map:
                map.add(num)
            else:
                map.remove(num)
        for i in map:
            return i