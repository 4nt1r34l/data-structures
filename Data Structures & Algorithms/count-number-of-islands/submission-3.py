class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        island = 0

        def dfs(r, c, ROWS, COLS, visit):
            row_in = 0<=r<ROWS
            col_in = 0<=c<COLS

            if not row_in or not col_in or grid[r][c] == '0' or (r,c) in visit:
                return False
            
            visit.add((r,c))

            for dr, dc in directions:
                newR, newC = dr+r, dc+c
                dfs(newR, newC, ROWS, COLS, visit)
            
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, ROWS, COLS, visit):
                    island+=1
        
        return island