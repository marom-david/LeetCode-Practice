class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            while n >= nums[i] > 0 and nums[i] != nums[nums[i] - 1]: 
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1