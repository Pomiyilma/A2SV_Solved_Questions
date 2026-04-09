class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        if not s:
            return [""]

        def isValid(string):
            count =0
            for char in string:
                if char== '(':
                    count +=1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        found = False
        res = []
        while queue:
            level_size =len(queue)
            current_level_valid = []
            
            for _ in range(level_size):
                curr =queue.popleft()
                
                if isValid(curr):
                    current_level_valid.append(curr)
                    found= True
                if not found:
                    for i in range(len(curr)):
                        if curr[i] not in "()":
                            continue
                        next_s = curr[:i] + curr[i+1:]
                        if next_s not in visited:
                            visited.add(next_s)
                            queue.append(next_s)
            
            if found:
                return current_level_valid

        return [""]
