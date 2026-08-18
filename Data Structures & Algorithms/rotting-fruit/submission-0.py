class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        
        while fresh and queue:
            length = len(queue)
            for _ in range(length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh-=1
            time+=1

        return time if not fresh else -1

