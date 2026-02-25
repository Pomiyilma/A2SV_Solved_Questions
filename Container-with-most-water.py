class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            w = right - left  #everytime we move the pointers to eachother, it decreases. wifth is the difference
            h = min(height[left], height[right])
            area = w * h
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1   #we keep right, move left
            else:
                right -= 1
        return max_area
