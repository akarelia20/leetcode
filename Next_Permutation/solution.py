def nextPermutation(nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
        print(i)
    if i == 0:       #if all the nums are in increasing order then reverse the array
            nums.reverse() 
            return
    z = i-1
    while nums[j] <= nums[z]:
        j -= 1
    temp = nums[z]
    nums[z] = nums[j]
    nums[j]= temp
    left= z+1
    right = len(nums)-1
    while right > left:
        nums[left], nums[right] = nums[right], nums[left]
        left +=1
        right -=1
    print(nums)

print(nextPermutation([3,2,1]))