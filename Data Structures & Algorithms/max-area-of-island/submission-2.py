class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        maxSize = 0

        def rowColCheck(r,c):
            row_in = 0<=r<ROWS
            col_in = 0<=c<COLS
            return row_in and col_in
        
        def dfs(r,c, ROWS, COLS, visit):
            if not rowColCheck(r,c) or (r,c) in visit or grid[r][c] == 0:
                return 0

            visit.add((r,c))

            size = 1
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                size += dfs(newR, newC, ROWS, COLS, visit)
            
            return size
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    size = dfs(r,c, ROWS, COLS, visit)
                    maxSize = max(maxSize, size)
        
        return maxSize