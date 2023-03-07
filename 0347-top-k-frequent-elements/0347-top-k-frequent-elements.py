class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                
        from heapq import heappush, heappop
        h = []
        for key in dict:
            heappush(h, (dict[key], key))
            if len(h) > k:
                heappop(h)
               
        res = []
        for freq, item in h:
            res.append(item)
        return res