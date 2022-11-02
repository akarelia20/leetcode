class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n= []
        temp= []
        
        for i in range(numRows):
            if i == 0:
                n.append([1])
            elif i == 1:
                n.append([1,1])
                
            else:
                for j in range(i+1):
                    if j == 0 or j == i:
                        temp.append(1)
                    else:
                        val = n[i-1][j-1] + n[i-1][j]
                        print(val)
                        temp.append(val)
                n.append(temp)
                temp = []

        return n