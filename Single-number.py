from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        for a in nums:
            if frequency[a] == 1:
                return a
