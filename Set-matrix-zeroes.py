class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)                         # exONnb
        n = len(matrix[0]) 
        rowZero = [False] * m
        colZero = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowZero[i] = True
                    colZero[j] = True
        for i in range(m):
            for j in range(n):
                if rowZero[i] == True or colZero[j] == True:
                    matrix[i][j] = 0    
