class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict= {}
        output= []
        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in dict:
                dict[sort] = [s]
            else:
                dict[sort].append(s)
        for key, val in dict.items():
            output.append(val)
                
        return output
                
        