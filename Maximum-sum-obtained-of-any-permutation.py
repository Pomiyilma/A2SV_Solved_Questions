class Solution:
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        MOD = 10**9 + 7
        res = 0
        
        freq = [0] * (n + 1)

        for l, r in requests:
            freq[l] += 1
            freq[r + 1] -= 1

        for i in range(1, n):
            freq[i] += freq[i - 1]

        freq = freq[:-1]

        nums.sort()
        freq.sort()

        for i in range(n):
            res += nums[i] * freq[i]
            res %= MOD

        return res
