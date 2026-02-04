from collections import Counter

class Solution:
    def isSubset(self, a, b):
        countA = Counter(a)
        countB = Counter(b)
        
        for elem in countB:
            if countA[elem] < countB[elem]:
                return False
        return True
