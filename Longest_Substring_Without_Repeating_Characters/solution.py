def lengthOfLongestSubstring(str):
    set = {}
    result= 0
    i = 0
    for j in range(len(str)):
        if str[j] in set:
            i = max(set[str[j]], i)
        set[str[j]] = j+1
        result = max(result, j-i+1)
    return result

print(lengthOfLongestSubstring("ertrgfv"))
