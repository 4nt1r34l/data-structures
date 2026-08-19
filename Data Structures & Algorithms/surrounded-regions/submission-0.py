class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque([])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r==0 or r==rows-1 or c == 0 or c == cols-1):
                    queue.append((r,c))
        
        while queue:
            r,c = queue.popleft()

            board[r][c] = 'T'

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == 'O':
                    queue.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'




        