class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def dfs(r,c):
            row_in = 0 <= r < rows
            col_in = 0 <= c < cols

            if not row_in or not col_in or grid[r][c] == '0' or (r,c) in visit:
                return
            
            visit.add((r,c))
            for nr, nc in directions:
                dr, dc = nr + r, nc + c
                dfs(dr, dc)
            
            return
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    island+=1
        
        return island