from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque([(sr,sc)])
        startColor = image[sr][sc]
        image[sr][sc] = color
        visit = set((sr,sc))
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS, COLS = len(image), len(image[0])

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                newR, newC = dr + row, dc + col
                
                if 0<=newR<ROWS and 0<=newC<COLS and (newR, newC) not in visit and (image[newR][newC] == startColor):
                    visit.add((newR, newC))
                    image[newR][newC] = color
                    queue.append((newR, newC))
        
        return image
