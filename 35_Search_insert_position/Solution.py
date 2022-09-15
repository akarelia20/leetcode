def searchInsert(nums , target):
    for i in range(len(nums)):
        if nums[i] > target and i == 0:
            return i
        elif nums[i] == target:
            return i
        elif len(nums)== 1 or nums[i+1] > target:
            return i+1
        elif nums[i+1] < target and i == len(nums)-2:
            return i+2


def SearchInsert2(nums, target):
    left,right = 0, len(nums)-1
    while left <= right:
        mid = (right+left)//2
        print(left, right, mid)
        if nums[mid]== target:
            return mid
        elif nums[mid] > target:
            right = mid -1
        elif nums[mid] < target:
            left = mid+1
    return left

print(SearchInsert2([1],0))