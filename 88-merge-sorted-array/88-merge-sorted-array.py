class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #tracks nums1 index backwards
        i= m-1
        # tracks nums2 index backwards
        j=n-1
        # tracks index of final nums1 array
        k=m+n-1
        
        while i>=0 and j>=0:
            # check the last number in both array and whichever one is grater place it 
            # at the kth index in nums[1]
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        print(nums1)
        if j>=0:
            nums1[:k+1]=nums2[:j+1]