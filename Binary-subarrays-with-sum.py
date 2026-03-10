class Solution:
    def numSubarraysWithSum(self, nums, goal):
        prefix, count = 0,0
        prefix_count = {0: 1}

        for num in nums:
            prefix += num

            if prefix - goal in prefix_count:
                count += prefix_count[prefix - goal]

            prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

        return count
