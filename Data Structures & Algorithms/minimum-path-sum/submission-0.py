class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def _max(grid, r, c, memo):
            pos = (r,c)

            if pos in memo:
                return memo[pos]

            if r >= len(grid) or c >= len(grid[0]):
                return float('inf')

            if r == len(grid)-1 and c == len(grid[0])-1:
                return grid[r][c]

            down = _max(grid, r+1, c, memo)
            right = _max(grid, r, c+1, memo)

            memo[pos] = grid[r][c] + min(down, right)

            return memo[pos]
        
        return _max(grid, 0, 0, {})