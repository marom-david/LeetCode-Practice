class Solution(object):
    def lengthOfLIS(self, nums):
        LIS_len = [1]*(len(nums))

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS_len[i] = max(LIS_len[i], LIS_len[j] + 1)  
                
        return max(LIS_len)
        