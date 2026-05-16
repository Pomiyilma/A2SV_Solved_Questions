class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                    board[r][c] = 'E'
                    queue.append((r, c))   
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in directions:
                next_r, next_c = curr_r + dr, curr_c + dc
                
                if 0 <= next_r < rows and 0 <= next_c < cols and board[next_r][next_c] == 'O':
                    board[next_r][next_c] = 'E'
                    queue.append((next_r, next_c))
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
