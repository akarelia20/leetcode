class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
#         stores letter and pos
        dict = {} 
        subStr_len= 0
#       tracks the starting index of substring
        i = 0
        
        for j in range(len(str)):
            if str[j] in dict:
                i = max(dict[str[j]], i)
            dict[str[j]]= j+1
            subStr_len= max(subStr_len, (j+1)-i)
        return subStr_len
        