class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def explore(grid, r, c, memo):
            if (r,c) in memo:
                return memo[(r,c)]
            
            if r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 1:
                return 0
            
            if r == len(grid)-1 and c == len(grid[0])-1:
                return 1
            
            memo[(r,c)] = explore(grid, r+1, c, memo) + explore(grid, r, c+1, memo)
            return memo[(r,c)]
        
        return explore(obstacleGrid, 0, 0, {})