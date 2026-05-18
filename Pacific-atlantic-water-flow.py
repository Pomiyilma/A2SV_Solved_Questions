class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        pacific_queue = deque()
        atlantic_queue = deque()
        pacific_visited = set()
        atlantic_visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific_queue.append((r, c))
                    pacific_visited.add((r, c))
                if r == ROWS - 1 or c == COLS - 1:
                    atlantic_queue.append((r, c))
                    atlantic_visited.add((r, c))
                    
        def bfs(queue, visited):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                curr_r, curr_c = queue.popleft()
                
                for dr, dc in directions:
                    next_r, next_c = curr_r + dr, curr_c + dc
                    if 0 <= next_r < ROWS and 0 <= next_c < COLS:
                        if (next_r, next_c) not in visited and heights[next_r][next_c] >= heights[curr_r][curr_c]:
                            visited.add((next_r, next_c))
                            queue.append((next_r, next_c))
                            
        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)
        
        return list(pacific_visited.intersection(atlantic_visited))
