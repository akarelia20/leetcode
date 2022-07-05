def wiggle_max_legnth(nums):
    high= 0
    low = 0
    final = 0
    diff = 0
    for i in range (0, len(nums)):
        print(f"final {final}")
        if nums[i] - nums[i-1] > 0:
            if nums[i]- nums[i-1] == diff:
                return 0
            elif nums[i] < high or i == len(nums)-1:
                final += 1
                high = 0
            elif nums[i] > high:
                if i==1:
                    final+= 1
                high = nums[i]
                diff = nums[i] - nums[i-1]
        elif nums[i] - nums[i-1] < 0:
            print(low)
            if nums[i] - nums[i-1] == diff:
                return 0
            elif nums[i] > low or i == len(nums)-1:
                final += 1
                low = 0
            elif nums[i] < low:
                low = nums[i]
                diff = nums[i] - nums[i-1]
        elif nums[i] - nums[i-1] == 0:
            return 0
    return final+1

print(wiggle_max_legnth([1,17, 5, 10, 13, 15, 10, 5, 15, 8]))

# print(wiggle_max_legnth([1,4,7,2,5]))

# print(wiggle_max_legnth([1,7,4,9,2,5]))