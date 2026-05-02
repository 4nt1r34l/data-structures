class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        
        def _count(grid, r, c, memo):
            if (r,c) in memo:
                return memo[(r,c)]

            if r >= len(grid) or c >= len(grid[0]):
                return 0

            if r == len(grid)-1 and c == len(grid[0])-1:
                return 1

            memo[(r,c)] = _count(grid, r+1, c, memo) + _count(grid, r, c+1, memo)
            return memo[(r,c)]
        
        return _count(grid, 0, 0, {})