class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            row = [0] + res[-1] + [0]
            curRow = []
            k = 0
            l = 1
            for j in range(len(res[-1])+1):
                curRow.append(row[k]+row[l])
                k+=1
                l+=1
            res.append(curRow)
        return res