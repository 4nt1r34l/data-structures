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
        
        def dfs(grid, r , c, ROWS, COLS, visit):
            if not rowColCheck(r,c) or (r,c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r,c))
            size = 1
            for x,y in directions:
                nr,nc = r+x, c+y
                size += dfs(grid, nr , nc, ROWS, COLS, visit)
            
            return size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    size = dfs(grid, r , c, ROWS, COLS, visit)
                    maxSize = max(maxSize, size)
        
        return maxSize