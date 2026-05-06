class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]

        def explore(grid, r, c, memo):
            if (r,c) in memo:
                return memo[(r,c)]
            
            if r >= m or c >= n:
                return 0
            
            if r == m-1 and c == n-1:
                return 1
            
            memo[(r,c)] = explore(grid, r+1, c, memo) + explore(grid, r, c+1, memo)
            return memo[(r,c)]
        
        return explore(grid, 0, 0, {})