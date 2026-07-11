class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r,c):
            row_in = 0 <= r < ROWS 
            col_in = 0 <= c < COLS

            if not row_in or not col_in or grid[r][c] == 0:
                return 1
            
            if (r,c) in visit:
                return 0

            visit.add((r,c))

            perim = 0
            for u,v in directions: 
                newR, newC = r+u, c+v
                perim += dfs(newR, newC)
            
            return perim
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r,c)
        
        return 0

