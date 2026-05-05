from heapq import heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def rowColCheck(r,c):
            row_in = 0 <= r < ROWS
            col_in = 0 <= c < COLS
            return row_in and col_in
        
        shortest = {} # [(r,c): cost]
        minHeap = [(grid[0][0], 0, 0)] # [(cost, r, c)]

        while minHeap:
            cost, row, col = heappop(minHeap)

            if not rowColCheck(row, col) or (row, col) in shortest:
                continue
            
            shortest[(row, col)] = cost

            if row == ROWS-1 and col == COLS-1:
                print(shortest)
                return max(shortest.values())

            for u,v in directions:
                new_row, new_col = row+u, col+v
                if rowColCheck(new_row, new_col):
                    heappush(minHeap, (grid[new_row][new_col], new_row, new_col))
        
        return -1
            
            
