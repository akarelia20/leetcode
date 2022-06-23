# given an array if integers in a sorted ascending order find the starting or ending position of a given number.
#  link to leetcode: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


# Runtime: 162 ms, Memory Usage: 15.4 MB


def binary_search (lo,hi,condition):
    while lo <= hi:
        mid = (lo+hi)//2
        result = condition(mid)
        print (result)
        if result =="found":
            return mid
        elif result== "left":
            hi = mid -1
        else:
            lo = mid+1
    return -1

def first_position(nums,target):
    def condition(mid):
        if nums[mid]== target:
            if mid > 0 and nums[mid-1] == target:
                return "left"
            return "found"
        elif nums[mid]<target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums)-1, condition)

def last_position(nums,target):
    def condition(mid):
        if nums[mid]==target:
            if mid < len(nums)-1 and nums[mid+1] ==target:
                return "right"
            return"found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position (nums,target):
    return first_position(nums,target), last_position(nums,target)

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return first_and_last_position(nums,target)

print(first_and_last_position([5,7,7,8,8,10,10], 8))