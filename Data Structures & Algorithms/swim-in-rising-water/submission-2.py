class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visit = set((0,0))
        min_heap = [(grid[0][0], 0, 0)] # [(value, row, col)]
        max_val = grid[0][0]

        def rowColCheck(r,c):
            row_in = 0 <= r < ROWS
            col_in = 0 <= c < COLS
            return row_in and col_in

        while min_heap:
            value, row, col = heapq.heappop(min_heap)

            max_val = max(max_val, value)

            if (row, col) == (ROWS-1, COLS-1):
                return max_val
            
            for nr, nc in directions:
                new_row, new_col = nr + row, nc + col
                if rowColCheck(new_row, new_col) and (new_row, new_col) not in visit:
                    heapq.heappush(min_heap, (grid[new_row][new_col], new_row, new_col))
                    visit.add((new_row, new_col))
        
        return -1
            

            