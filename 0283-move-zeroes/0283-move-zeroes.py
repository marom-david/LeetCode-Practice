class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) < 2:
            return nums
        zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1

                            
        return nums
             
        