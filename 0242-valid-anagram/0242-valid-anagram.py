class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        if len(s) == len(t):
            for i in s:
                if i not in s_dict:
                    s_dict[i] = 1
                else:
                    s_dict[i] += 1
                    
            for j in t:
                if j in s_dict:
                    s_dict[j] -= 1
                    if s_dict[j] == 0:
                        s_dict.pop(j)
                else:
                    return False
            if s_dict== {}:
                return True
                