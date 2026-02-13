class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = Counter(ransomNote)
        count_magazine = Counter(magazine)

        for char in count_ransom:
            if count_ransom[char] > count_magazine[char]:
                return False
        return True
