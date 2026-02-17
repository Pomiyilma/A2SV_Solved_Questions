class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        if mat == target: #we checking 0 deg rotation
            return True

        if all(mat[r][c] == target[c][n - 1 - r] #90 deg (r, c) moves to (c, n-1-r)
               for r in range(n) for c in range(n)):
            return True

        if all(mat[r][c] == target[n - 1 - r][n - 1 - c] #180 deg (r,c) moves to (n-1-r, n-1-c)
               for r in range(n) for c in range(n)):
            return True

        if all(mat[r][c] == target[n - 1 - c][r] #270 degree (r, c) moves to (n-1-c, r)
               for r in range(n) for c in range(n)):
            return True

        return False
