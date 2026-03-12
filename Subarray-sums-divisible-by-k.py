class Solution:
    def subarraysDivByK(self, nums, k):

        count = {0: 1}
        prefix_sum, res = 0,0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in count:
                res += count[remainder]
            count[remainder] = count.get(remainder, 0) + 1

        return res
