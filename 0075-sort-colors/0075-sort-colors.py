class Solution(object):
    def sortColors(self, nums):
        if len(nums) < 2:
            return nums
        
        two = 0
        for i in range(len(nums)):
            if nums[i] != 2:
                nums[two], nums[i] = nums[i], nums[two]
                two += 1

        one = 0
        for i in range(two):
            if nums[i] != 1:
                nums[one], nums[i] = nums[i], nums[one]
                one += 1
                            
        return nums 
        