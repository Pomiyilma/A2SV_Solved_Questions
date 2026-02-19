#from functools import cmp_to_key   What do they do
class Solution:
    def largestNumber(self, nums: List[int]) -> str:               #exONnb
        nums = list(map(str, nums))
        def compare(a, b):
            if a + b > b + a:   #means 'a' comes first eg: a=34 b=3, 343 is bigger than 334
                return -1
            elif b + a > a + b:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == "0":
            return "0"
        return "".join(nums)
