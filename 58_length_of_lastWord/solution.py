def lengthOfLastWord(s):
    count= 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == " " and count != 0:
            break
        elif s[i] == " ":
            continue
        else:
            count+=1
    return count


print(lengthOfLastWord("  fly me to the moon   "))
        