def jump(nums):
    if len(nums) <= 1: 
        return 0
    left = 0
    right = nums[0]
    jump_count = 1
    while right < len(nums) - 1:
        jump_count += 1
        next = max(i + nums[i] for i in range(left, right + 1))
        left, right = right, next
    return jump_count

print(jump([2,1,1,3,4]))