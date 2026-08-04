from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque([(r, c, 0) for r in range(rows) for c in range(cols) if grid[r][c] ==  0])

        while queue:
            r , c, dist = queue.popleft()

            for u,v in directions:
                newR, newC = u+r, v+c
                if 0<=newR<rows and 0<=newC<cols and grid[newR][newC] == INF:
                    grid[newR][newC] = dist + 1
                    queue.append((newR, newC, dist+1))
                    