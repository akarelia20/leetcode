class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map={}
        compare=set()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            # print(s[i])
            if s[i] not in map:
                map[s[i]] = t[i]
                compare.add(t[i])
                print(compare)
            else:
                if map[s[i]] != t[i]:
                    return False
        if len(compare) != len(map):
            return False
        return True