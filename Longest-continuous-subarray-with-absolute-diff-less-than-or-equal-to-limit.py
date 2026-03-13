class Solution:
    def longestSubarray(self, nums, limit):
        maxD = deque()
        minD = deque()

        left,res = 0, 0
        for right in range(len(nums)):
            while maxD and nums[right] > maxD[-1]:
                maxD.pop()

            while minD and nums[right] < minD[-1]:
                minD.pop()
            maxD.append(nums[right])
            minD.append(nums[right])

            while maxD[0] - minD[0] > limit:
                if maxD[0] == nums[left]:
                    maxD.popleft()

                if minD[0] == nums[left]:
                    minD.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res
