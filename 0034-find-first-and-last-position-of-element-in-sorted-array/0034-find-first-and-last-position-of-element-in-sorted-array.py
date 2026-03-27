class Solution(object):
    def searchRange(self, nums, target):
        left = -1
        right = -1
        result = []
        l = 0
        r = len(nums) - 1

        while l <= r:
            index = (l+r)//2
            if nums[index] == target:
                left = index
                r = index - 1
            if nums[index] > target:
                r = index - 1
            if nums[index] < target:
                l = index + 1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            index = (l+r)//2
            if nums[index] == target:
                right = index
                l = index + 1
            if nums[index] > target:
                r = index - 1
            if nums[index] < target:
                l = index + 1

        return [left,right]