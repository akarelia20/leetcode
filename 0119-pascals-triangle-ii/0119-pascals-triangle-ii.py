class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n= []
        
        for i in range(rowIndex+1):
            if i == 0:
                n.append([1])
            elif i == 1:
                n.append([1,1])
                
            else:
                for j in range(i+1):
                    if j == 0:
                        n.append([1])
                    elif j == i:
                        n[i].append(1)
                    else:
                        val = n[i-1][j-1] + n[i-1][j]
                        n[i].append(val)
        return n[rowIndex]