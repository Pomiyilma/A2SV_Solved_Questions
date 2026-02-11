from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = Counter(s)
        freq_t = Counter(t)

        steps = 0
        for ch in freq_s:
            if freq_s[ch] > freq_t[ch]:           #if t is short in That char:
                steps += freq_s[ch] - freq_t[ch]

        return steps

        
