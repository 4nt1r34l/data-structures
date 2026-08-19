class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        atlantic = set()
        pacific = set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visit):
            visit.add((r,c))
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit and heights[nr][nc] >= heights[r][c]:
                    visit.add((nr,nc))
                    dfs(nr, nc, visit)
        
        for r in range(rows):
            dfs(r, 0, pacific) # left column, pacific
        
        for r in range(rows):
            dfs(r, cols-1, atlantic) # right column, atlantic

        for c in range(cols):
            dfs(0, c, pacific) # top row, pacific
        
        for c in range(cols):
            dfs(rows-1, c, atlantic) # bottom row, atlantic
        
        return list(pacific & atlantic)