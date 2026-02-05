from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)

            for ch in word_count:
                if word_count[ch] > chars_count[ch]:
                    break
            else:
                total_length += len(word)

        return total_length
        
