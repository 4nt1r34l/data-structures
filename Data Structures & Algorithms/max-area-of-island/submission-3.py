class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0

        def dfs(r,c):
            row_in = 0 <= r < ROWS
            col_in = 0 <= c < COLS

            if not row_in or not col_in or (r,c) in visit or grid[r][c] == 0:
                return 0

            visit.add((r,c))
            size = 1
            for u,v in directions:
                nr, nc = r+u, c+v
                size += dfs(nr, nc)

            return size 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    size = dfs(r,c)
                    maxArea = max(maxArea, size)
        
        return maxArea
