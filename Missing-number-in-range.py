class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        #called Gauss's Summation formula (works everytime when range sum is involved !)

        expected_sum = n * (n + 1) // 2   
        actual_sum = sum(nums)
        return expected_sum - actual_sum
