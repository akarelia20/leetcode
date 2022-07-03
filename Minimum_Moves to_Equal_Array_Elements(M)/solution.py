
# Runtime: 104 ms, faster than 67.89% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
# Memory Usage: 15.6 MB, less than 6.80% of Python3 online submissions for Minimum Moves to Equal Array Elements II.


def min_moves(nums): 
    # sort the list
    nums = sorted(nums)
    # find the middle element of h]the sorted list
    median = nums[len(nums)//2]
    print(median)
    moves = 0
    # itrate through the list
    for i in nums:
        # add diffrece of each element from middle elements value to moves
        moves += abs(median - i)
    # finally return the moves 
    return moves

print(min_moves([0,0,0,100,102]))
print(min_moves([45,45,100,102]))