def wiggle_max_legnth(nums):
    hi = 0
    low =0
    for i in range(1, len(nums)):
        # current element could be higest
        if nums[i - 1] < nums[i]:
            hi = low + 1
        # current element could be lowest
        elif nums[i - 1] > nums[i]:
            low = hi + 1
    # add 1 because we didn't count the first element
    return 1 + max(hi, low)



