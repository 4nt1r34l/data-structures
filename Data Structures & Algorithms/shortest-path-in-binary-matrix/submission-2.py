class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visit = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([(0,0,1)])
        end = (ROWS-1, COLS-1)

        if grid[0][0] == 1:
            return -1

        while queue:
            r, c, short = queue.popleft() 
            
            if (r,c) == end:
                return short

            for u,v in directions:
                nr, nc = r + u, c + v
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    queue.append((nr, nc, short+1))
            
        return -1
        