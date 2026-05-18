class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visit = set()
        heap = [(0,0,0)] # (diff, r, c)
        ROWS, COLS = len(heights), len(heights[0])

        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r,c) in visit:
                continue
            
            visit.add((r,c))
            
            if r == ROWS-1 and c == COLS-1:
                return diff
            
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0<=newR<ROWS and 0<=newC<COLS and (newR, newC) not in visit:
                    newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                    heapq.heappush(heap, (newDiff, newR, newC))
            
        return 0
            
