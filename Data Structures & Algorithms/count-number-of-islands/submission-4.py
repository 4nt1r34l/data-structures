class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        directions = [(0,1), (1,0), (-1, 0), (0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        island = 0

        def dfs(grid, r , c, ROWS, COLS, visit):
            row_in = 0 <= r < ROWS
            col_in = 0 <= c < COLS

            if not row_in or not col_in or (r,c) in visit or grid[r][c] == '0':
                return False
            
            visit.add((r,c))

            for x,y in directions:
                nr,nc = r+x, c+y
                dfs(grid, nr, nc, ROWS, COLS, visit)
            
            return True

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    if dfs(grid, r , c, ROWS, COLS, visit):
                        island+=1
        
        return island