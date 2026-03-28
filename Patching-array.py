class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1         #smallest num we have to form
        patches, i = 0,0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
                
        return patches
