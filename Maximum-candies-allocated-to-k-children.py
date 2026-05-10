class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        def canAllocate(size):
            if size == 0: return True
            count = 0
            for pile in candies:
                count += pile // size
            return count >= k

        low = 1
        high = sum(candies) // k
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if canAllocate(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
