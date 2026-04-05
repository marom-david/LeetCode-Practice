class Solution(object):
    def maxProduct(self, nums):
        max_sum = nums[0]
        min_sum = nums[0]
        global_sum = nums[0]

        for i in range(1, len(nums)):
            max_sum, min_sum= max(nums[i], nums[i]*max_sum, nums[i]*min_sum), min(nums[i], nums[i]*min_sum, nums[i]*max_sum)
            global_sum = max(max_sum, min_sum, global_sum)
        
        return global_sum
