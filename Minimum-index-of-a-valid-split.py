class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)    #{2:2, 1:6, 3:1, 7:1}
        #if nums doesn't have dom elem- Counter(nums).values() !> n/2) :
            #return -1
        dominant = None
        for num, freq in count.items():
            if freq > (len(nums) // 2):
                dominant = num
                break
        if dominant is None:
            return -1

        left_count = 0
        total_count = count[dominant]

        for i in range (len(nums) - 1): #[2,1,3,1,1,1,7,1,2,1]
            if nums[i] == dominant:
                left_count += 1
            left_length = i + 1
            right_length = len(nums) - left_length
            right_count = total_count - left_count

            if(left_count > left_length // 2 and right_count > right_length // 2):
                return i
        return -1
