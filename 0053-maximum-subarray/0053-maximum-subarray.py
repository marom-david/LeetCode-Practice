class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = (nums[0])
        max_sum = (nums[0])

        for n in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[n], nums[n])
            max_sum = max(max_sum, curr_sum)

        return max_sum
        