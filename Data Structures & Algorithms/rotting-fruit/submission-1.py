class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        minute = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue and fresh>0:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()

                for u,v in directions:
                    nr, nc = row+u, col+v
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1:
                        fresh-=1
                        queue.append((nr,nc))
                        grid[nr][nc] = 2
                
            
            minute+=1
        
        return minute if fresh==0 else -1
        

