class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)                            #exONnb   
        cols = len(matrix[0])
        result = []

        def helper(top, bottom, left, right):
            if top > bottom or left > right:
                return    # the Base case
            for col in range(left, right + 1):
                result.append(matrix[top][col])

            for row in range(top + 1, bottom + 1):
                result.append(matrix[row][right])

            if top < bottom:
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][col])

            if left < right:
                for row in range(bottom - 1, top, -1):
                    result.append(matrix[row][left])

            helper(top + 1, bottom - 1, left + 1, right - 1)

        helper(0, rows - 1, 0, cols - 1)
        
        return result
