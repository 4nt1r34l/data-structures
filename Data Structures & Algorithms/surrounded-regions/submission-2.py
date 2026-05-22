class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, ROWS, COLS, visit):
            row_in = 0 <= r < ROWS 
            col_in = 0 <= c < COLS

            if not row_in or not col_in or board[r][c] in visit or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                dfs(newR, newC, ROWS, COLS, visit)
            
            return

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r==0 or c == 0 or r == ROWS-1 or c == COLS-1):
                    dfs(r, c, ROWS, COLS, visit)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

        

        
