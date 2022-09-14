def removeDuplicates(nums):
    counter= 0
    for i in range(len(nums)-1):
        if nums[i] != nums[i-1]:
            nums[counter]= nums[i]
            counter+=1
    return counter

print(removeDuplicates([1,1,2,2,4,4,4]))