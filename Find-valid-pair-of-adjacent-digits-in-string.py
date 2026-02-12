from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        
        for i in range(len(s) - 1):
            if (
                s[i] != s[i + 1] and
                freq[s[i]] == int(s[i]) and
                freq[s[i + 1]] == int(s[i + 1])
            ):
                return s[i] + s[i + 1]
        
        return ""
