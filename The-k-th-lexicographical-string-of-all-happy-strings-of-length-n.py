class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        path = []

        def backtrack():
            if len(result) >= k:
                return

            if len(path) == n:
                result.append("".join(path))
                return

            for ch in ['a', 'b', 'c']:
                if path and path[-1] == ch:
                    continue

                path.append(ch)
                backtrack()
                path.pop()

        backtrack()

        if len(result) < k:
            return ""
        return result[k - 1]
