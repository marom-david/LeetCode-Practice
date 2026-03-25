class Solution(object):
    def maxArea(self, height):
        max_sum = 0
        curr_sum = 0 
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] < height[right]:
                curr_sum = (height[right]*(right - left)) - ((height[right]-height[left])*(right - left))
                left += 1
            else:
                curr_sum = (height[left]*(right - left)) - ((height[left]-height[right])*(right - left))
                right -= 1
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

            