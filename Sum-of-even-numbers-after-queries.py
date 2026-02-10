class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        result = []

        for num in nums:         #exONnb
            if num % 2 == 0:
                even_sum += num

        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            result.append(even_sum)
        return result
