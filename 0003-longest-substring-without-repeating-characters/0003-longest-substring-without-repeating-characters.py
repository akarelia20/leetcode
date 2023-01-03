class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        dict = {}
        result= 0
        i = 0
        for j in range(len(str)):
            if str[j] in dict:
                i = max(dict[str[j]], i)
            dict[str[j]] = j+1
            result = max(result, j-i+1)
        return result