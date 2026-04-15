class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        #SUBSEQUENCE != SUBARRAY btw

        #nums = [4, 6, 7, 7]
        # def backtrack(...):
        #ALWAYS IN BACKTRACK
        #     if basecase:
        #         save ans
        #     for choice in choices:
        #         choose
        #         backtrack(...)
        #         unchoose/pop
        res, path = [], []
        def backtrack(start):
            if len(path) >= 2:
                res.append(path[:])  #appending shallow copy because path will later be mOdiFied. 
            used = set()
            for i in range(start,len(nums)):
                if nums[i] in used:
                    continue
                if path and nums[i] < path[-1]:
                    continue

                used.add(nums[i])

                path.append(nums[i]) #choose
                backtrack(i + 1) #backtrack
                path.pop() #unchoose
        backtrack(0)
        return res
