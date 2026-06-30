class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setRow = set()
        setCol = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    setRow.add(r)
                    setCol.add(c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in setRow or c in setCol:
                    matrix[r][c] = 0
        
        