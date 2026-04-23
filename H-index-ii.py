class Solution:
    def hIndex(self, citations: List[int]) -> int:    #exONnb
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= len(citations) - mid:   #THE MAIN THING
                right = mid - 1
            else:
                left = mid + 1

        return len(citations) - left
