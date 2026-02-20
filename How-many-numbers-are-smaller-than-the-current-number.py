class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):     #nums = [8,1,2,2,3], nums[i] = 8
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result[i] = count
        return result
        
