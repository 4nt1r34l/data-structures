class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        island = 0

        def dfs(r,c):
            row_in = 0 <= r < ROWS
            col_in = 0 <= c < COLS

            if not row_in or not col_in or (r,c) in visit or grid[r][c] == "0":
                return False
            
            visit.add((r,c))
            
            for u,v in directions:
                nr, nc = r+u, c+v
                if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visit and grid[nr][nc] == "1":
                    dfs(nr,nc)
            
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    if dfs(r,c):
                        island+=1
        
        return island
