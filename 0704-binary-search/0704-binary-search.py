class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        index = (l+r)//2

        while l <= r:
            index = (l+r)//2
            if nums[index] == target:
                return index
            if nums[index] > target:
                r -= 1
            if nums[index] < target:
                l += 1
        
        return -1