class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        
        directions = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,-1),(-1, 1),(1, 1)]
        queue = deque([(0, 0, 1)])
        rows, cols = len(grid), len(grid[0])
        visit = set((0,0))

        while queue:
            r, c, dist = queue.popleft()

            if r == rows-1 and c == cols-1:
                return dist
            
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                if 0<=newR<rows and 0<=newC<cols and not grid[newR][newC] and (newR, newC) not in visit:
                    visit.add((newR, newC))
                    queue.append((newR, newC, dist + 1))
        
        return -1