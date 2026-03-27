class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            index = (l+r)//2
            if nums[index] == target:
                return index
            if nums[index] > target:
                r = index - 1
            if nums[index] < target:
                l = index + 1
        
        return -1