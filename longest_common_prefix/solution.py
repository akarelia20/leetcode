def longestCommonPrefix(strs):
    result= ""
    j=0
    x = len(min(strs, key=len))
    print(x)
    match = True
    if len(strs) ==1:
        return strs[0]
    while x > 0 and match == True:
        for i in range (1, len(strs)):
            # print(result)
            if strs[i-1][j] == strs[i][j]:
                match =True
                if i == len(strs)-1:
                    result += strs[i][j]
                    j +=1
                    x -= 1   
            elif strs[i-1][j] != strs[i][j]:
                match= False
                break
    return result

# MORE EFFICIENT 
# Runtime: 39 ms, faster than 85.52% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.9 MB, less than 88.10% of Python3 online submissions for Longest Common Prefix.

def longestCommonPrefix(strs):
        result=""
        if len(strs[0]) == 0:
            return result
        for i in range(len(min(strs))):
            char = strs[0][i]
            # The all() function returns True if all items in an iterable are true
            if all(x[i] == char for x in strs):
                result += char
            else: 
                break
        return result
        

print(longestCommonPrefix(["flower88", "flower", "flower"]))

