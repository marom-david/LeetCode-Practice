class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for r in range(len(nums)):
            res[r] = prefix
            prefix *= nums[r]

        suffix = 1
        for l in range(len(nums) - 1, -1, -1):
            res[l] *= suffix
            suffix *= nums[l]

        return res