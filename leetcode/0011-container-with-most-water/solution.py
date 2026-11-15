class Solution:
    def maxArea(self, height: list[int]) -> int:
        #go through each line and calculate max area with all other lines?
        max = 0
        left = 0
        right = len(height)-1
        while (left < right):
            area = min(height[left],height[right])*(right-left)
            if area > max:
                max = area
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max

