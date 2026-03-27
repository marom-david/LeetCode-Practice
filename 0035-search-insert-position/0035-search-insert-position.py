class Solution(object):
    def searchInsert(self, nums, target):
        r = len(nums) - 1
        l = 0
        index = (l+r)//2

        while l <= r:
            index = (l+r)//2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                r = index - 1
            elif nums[index] < target:
                l = index + 1
        
        return l