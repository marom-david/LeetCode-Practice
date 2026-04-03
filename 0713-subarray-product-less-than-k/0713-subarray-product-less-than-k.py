class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        res = 0
        product = 1
        l = 0

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k and l <= r:
                product /= nums[l]
                l += 1

            res += (r-l+1)
            
        return res