# if we follow the fibonacci pattern
# [1,2,3,4,5] => [1,2,3,5,8] where LAST STEP 8 is IS SUM OF PERV TWO NUMS 3+5 =>8
# meaning possible ways to get to last step is sum of possible ways to get to second last step and last to last step
# possible ways(n)= possible ways(n-1)+ possible ways(n-2)


def climbStarirs(n):
    if n <=2:
        return n
    possible_ways= 0
    # consider 3 is our basecase
    OneStep_down= 2 # to get to 3 => 1 step down is 2
    TwoStep_down= 1 # and two step down is 1
    for i in range(3, n+1):
        possible_ways = OneStep_down + TwoStep_down
        # now we will move upto n and only remmember ways to get to last two steps
        # and swap them
        TwoStep_down = OneStep_down
        OneStep_down = possible_ways
    return possible_ways


print(climbStarirs(5))