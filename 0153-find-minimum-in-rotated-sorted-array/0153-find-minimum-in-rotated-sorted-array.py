class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        index = (l+r)//2
        
        while l < r:
            index = (l+r)//2
            if nums[index] > nums[r]:
                l = index + 1
            else:
                r = index
              
        return nums[l]