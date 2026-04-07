class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n                           #exONnb
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid   
            else:
                left = mid + 1
        return left
