find the question here:
https://leetcode.com/problems/non-decreasing-array/

Strategy:
Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

if Input Array - [3, 4, 2, 3]
Here if you see, there is only one violation at index 2.
Fixed violation at index 2 - [3, 2, 2, 3]

But after fixing the violation, the array is still not in non-decreasing order. Hence, it's an invalid case. So from this example we can observe that we need to take into account nums[i-2] as well.

From the above details, we can observe the following:

We need the count of violations in the input array. If at any point count > 1, we return False
For any violation, we have to make an additional check for nums[i-2]. If nums[i-2]>nums[i], we perform nums[i]=nums[i-1] to fix the violation.
