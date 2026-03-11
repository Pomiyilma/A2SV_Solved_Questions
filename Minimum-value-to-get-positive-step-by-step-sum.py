class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pref, min_pref = 0,0
        for num in nums:
            pref += num
            min_pref = min(pref, min_pref)
        return  1 - min_pref  #so that startValue + smallest prefix ≥ 1
