class Solution(object):
    def minSubArrayLen(self, target, nums):
        l, min_size, curr_sum = -1, float('inf'), 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                if min_size > r - l:
                    min_size = r - l
                l += 1
                curr_sum -= nums[l]
        
        if min_size == float('inf'):
            return 0 
        
        return min_size

        