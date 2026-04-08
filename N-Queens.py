class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # no queens attack eachother = same row = same col = same diagonal
        # diff row, diff col, diff diagonal.
        # approach : placing every queen in every col of a row => check validity => if valid move to the next row => if not, next pos

        # def solve(row, board):
        #     if row == n:
        #         res.add(board)
        #         return
        #     for col from 0 to n - 1:
        #         if isValid(board, col, row):
        #             place queen @ (row, col)
        #             solve(row + 1, board)
        #             remove queen from (row, col)     BASIC BACKTRACKING STEPS
        # def isValid(board, col, row):
        #     check column staright above
        #     check upper-left diagonal
        #     check upper-right diagonal
        #     if safe:
        #         return true

        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):

            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):

                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
