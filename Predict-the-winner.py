class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}

        def dfs(l, r):
            if l == r:
                return nums[l]
            
            if (l, r) in dp:
                return dp[(l, r)]

            take_left = nums[l] - dfs(l + 1, r)
            take_right = nums[r] - dfs(l, r - 1)
            
            dp[(l, r)] = max(take_left, take_right)
            return dp[(l, r)]
        
        return dfs(0, n - 1) >= 0
