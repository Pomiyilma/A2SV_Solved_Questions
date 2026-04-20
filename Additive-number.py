class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(a, b, start):
            while start < n:
                s = a + b
                s_str = str(s)

                
                if not num.startswith(s_str, start): #if next part matches
                    return False
                start += len(s_str)
                a, b = b, s
            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                a = num[:i]
                b = num[i:j]

                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue
                if valid(int(a), int(b), j):
                    return True

        return False
