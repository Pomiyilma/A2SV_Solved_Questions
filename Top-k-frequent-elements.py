from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        #exONnb
        freq = Counter(nums) 
        sorted_nums = sorted(freq.items(), key=lambda x:x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(sorted_nums[i][0])
        return result
