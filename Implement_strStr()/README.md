Implement strStr().

- Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

### Clarification:

- What should we return when needle is an empty string? This is a great question to ask during an interview.

- For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


- Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

- Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


### time and space complexity
- Runtime: 49 ms, faster than 47.76% of Python3 online submissions for Implement strStr().
- Memory Usage: 14 MB, less than 15.38% of Python3 online submissions for Implement strStr().