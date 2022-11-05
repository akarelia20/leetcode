class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n= []
        temp= []
        
        for i in range(rowIndex+1):
            if i == 0:
                n.append([1])
            elif i == 1:
                n.append([1,1])
                
            else:
                for j in range(i+1):
                    if j == 0 or j == i:
                        temp.append(1)
                    else:
                        print(n[i-1][j-1] + n[i-1][j])
                        val = n[i-1][j-1] + n[i-1][j]
                        temp.append(val)
                n.append(temp)
                temp = []
                    
        print(n)
        return n[rowIndex]
        