class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        count = {}              #chars freq in a window
        left, max_freq, max_length = 0, 0, 0    

        for right in range(len(s)):  #expand window
            count[s[right]] = count.get(s[right], 0) + 1  #current character to frequency map
            max_freq = max(max_freq, count[s[right]])
            window_size = right - left + 1

            if window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length
