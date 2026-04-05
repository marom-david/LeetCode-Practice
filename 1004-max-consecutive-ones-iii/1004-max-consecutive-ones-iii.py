class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        curr_cons = 0
        zero = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero += 1
            while zero > k:
                if nums[l] == 0:
                    zero -= 1       
                l += 1
            curr_cons = max(curr_cons, r-l+1)

        return curr_cons