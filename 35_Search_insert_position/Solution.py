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
