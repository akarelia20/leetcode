def strStr(haystack,needle):
    if needle == "":
        return 0
    elif len(needle) > len(haystack):
        return -1
    for y in range(len(needle)):
        for i in range(len(haystack)):
            if needle[y] == haystack[i] and needle == haystack[i:i+len(needle)]: 
                return i
        return -1

print(strStr("hello","ll"))  
