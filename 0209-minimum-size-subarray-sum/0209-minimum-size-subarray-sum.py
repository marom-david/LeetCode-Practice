class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        current_sum = 0
        min_idx = len(nums) + 1

        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                min_idx = min(min_idx, r-l+1)
                current_sum -= nums[l]
                l += 1
            
        return min_idx if min_idx != len(nums) + 1 else 0
        