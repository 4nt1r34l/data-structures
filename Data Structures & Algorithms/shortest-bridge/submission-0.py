class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        queue = deque([])

        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if grid[nr][nc] == 0:
                        visited.add((nr, nc))
                        queue.append((nr, nc, 1))
                    else:
                        dfs(nr, nc)

        break_all = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break_all = True
                    break

            if break_all:
                break
        
        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                if 0<=newR<rows and 0<=newC<cols and (newR,newC) not in visited:
                    if grid[newR][newC] == 1:
                        return dist
                    visited.add((newR, newC))
                    queue.append((newR, newC, dist+1))
        
