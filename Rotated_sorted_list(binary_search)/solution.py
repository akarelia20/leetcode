# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Runtime: 64 ms, faster than 44.15% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.4 MB, less than 23.07% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

# ==========================================================================================================
# 1. define hi and low indeces to keep track of the search size, at the beginning hi is len(arr)-1 and low is 0
# 2. set the mid point which is arr_length//2
# 3. if the value of the mid point is higer than the last elememnt of the array than we know that the lowest value 
#  resides at the right half of the array and if the mid point is lower than the last element that the lowest value resides in 
#  the left of the mid point.
# 4. repeate the seach till we find the lowest number.
# 5. after the successful find return the index of the lowest value in the array.
# --- in the above example lowest num is 1, at that is at idx 3 which means list was roted 3 times-----

# ==================================================================================================================

def find_min(nums):
    low = 0
    hi= len(nums)-1
    if nums[hi] > nums[low] or len(nums) ==1:
            return nums[0]
    while low <= hi:
            mid = (low+hi)//2
            mid_num = nums[mid] 
            print(low, hi, mid, mid_num)
            if mid_num > nums[mid+1]:
                return nums[mid+1]
            if nums[len(nums)-1]<  mid_num:
                low = mid+1 # right side(end of the arr)
            elif nums[len(nums)-1] > mid_num:
                hi = mid-1 # left side (beginning of the arr)
    return mid_num

print(find_min([3,1,2]))


