def checkPossibility(nums):
    # checks if current-idx is higetr than next-idx
    counter= 0
    # starts at idx 1
    for i in range(1,len(nums)):
        if  nums[i-1] > nums[i]:
            if counter ==1 :
                return False
            counter+=1
            # if current index is 2 or greater and current element is lower than it previous to previous element than 
            # set current element value to previous elements value
            if i>=2 and nums[i-2]>nums[i]:
                nums[i] = nums[i-1]
    return True
    
            
print(checkPossibility([1,5,2,4,3]))
