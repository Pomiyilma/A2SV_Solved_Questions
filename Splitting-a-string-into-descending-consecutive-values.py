class Solution:
    def splitString(self, s: str) -> bool:                 #exONnb
        def dfs(index, prev):
            if index == len(s):
                return True
            for j in range(index, len(s)):
                val = int(s[index:j+1])
                if val + 1== prev and dfs(j+1, val):
                    return True
            return False
        for i in range(0, len(s)-1):
            val = int(s[:i+1])
            if dfs(i+1, val):
                return True
        return False


        # def split(path, i):
        #     if i == len(s):
        #         for i in range(1, len(path)):
        #             if path[i] != path[i-1] - 1:
        #                 return False
        #         return len(path) >= 2

        #     for j in range(i, len(s)):
        #         val = int(s[i : j+1])
        #         path.append(val)
        #         if split(path, j + 1):
        #             return True
        #         path.pop()
        #     return False
        # return split([], 0)
