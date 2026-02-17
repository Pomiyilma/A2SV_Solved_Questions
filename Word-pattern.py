class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:              #exONnb
        words = s.split()
        char_to_word = {}
        used_words = set()

        if len(words) != len(pattern):            
            return False

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                if word in used_words:
                    return False
                char_to_word[char] = word
                used_words.add(word)
        return True
