class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #right, down, left, up
        
        r, c = rStart, cStart
        result = [[r, c]]
        
        step_size = 1
        dir_idx = 0 #starting with right (b/c 0,1,2,3 means r,d,l,u)

        while len(result) < rows * cols:
            # Repeat twice for each step size increment
            for _ in range(2):
                dr, dc = directions[dir_idx]
                for _ in range(step_size):
                    r += dr
                    c += dc
   
                    if 0 <= r < rows and 0 <= c < cols: #if current position is inside the grid boundaries
                        result.append([r, c])
                        
                dir_idx = (dir_idx + 1) % 4  #b/c there are 4 dxns
            step_size += 1  #every 2 dxns
        return result
