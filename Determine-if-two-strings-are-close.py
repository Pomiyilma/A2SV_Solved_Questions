class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        word1_val = Counter(word1).values()
        word2_val = Counter(word2).values()
        if sorted(word1_val) != sorted(word2_val):   #without sortinG, it may fail
            return False
        return True
