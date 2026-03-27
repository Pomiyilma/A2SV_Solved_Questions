class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combo_dict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []
        def backtrack(index, combo):
            if index == len(digits):
                res.append(combo)
                return
            letters = combo_dict[digits[index]]

            for letter in letters:
                combo += letter
                backtrack(index + 1, combo)
                combo = combo[:-1]

        backtrack(0, "")
        return res
