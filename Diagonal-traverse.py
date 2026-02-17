class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        result = []

        for d in range(rows + cols - 1):   #inserting 3x3 as an example to know why -1
            temp = []
            if d < rows:
                r = d
                c = 0
            else:
                r = rows - 1
                c = d - (rows - 1)

            while r >= 0 and c < cols:  #moving up-right (row decreases, column increases)
                temp.append(matrix[r][c])
                r -= 1
                c += 1

            if d % 2 == 1:   #if odd, down-left (reeverse)
                result.extend(temp[::-1])
            else:     #if even, Keep up-right traversal
                result.extend(temp)
                
        return result
