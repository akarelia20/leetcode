# leetcode link : https://leetcode.com/problems/remove-element/
# Runtime: 50 ms, faster than 71.79% of Python3 online submissions for Remove Element.
# Memory Usage: 13.9 MB, less than 62.27% of Python3 online submissions for Remove Element.


def remove_element(nums, val):
    k =0
    for i in range (0, len(nums)):
        # if i matches with value then continue
        if nums[i] == val:
            continue
        # if i doesn't match then only add those to the nums array by nums[k] = num[i]
        # k keeps track of the nums whose value doesnt match with the value that is passed in
        else:
            nums[k] = nums[i]
            k +=1
        print(nums)
    return k, nums


print(remove_element([2,2,1,8,1,0], 1))
