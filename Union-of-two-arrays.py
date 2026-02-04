class Solution:    
    def findUnion(self, a, b):
        union = set(a)
        union.update(set(b))
        
        return union
