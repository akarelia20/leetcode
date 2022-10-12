class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        for i in t:
            if counter == len(s):
                break
            if i == s[counter]:
                counter +=1
        print(counter)   
        if counter == len(s):
            return True
        return False