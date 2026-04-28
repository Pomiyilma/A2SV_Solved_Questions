class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):
            D, curr = 1,0
            for w in weights:
                if curr + w > capacity:
                    D += 1
                    curr = 0
                curr += w
            return D <= days

        left, right = max(weights),sum(weights)

        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid 
            else:
                left = mid + 1
        return left
