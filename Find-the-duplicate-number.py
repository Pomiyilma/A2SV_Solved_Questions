class Solution:
    def findDuplicate(self, nums):
        left, right = 1, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left
