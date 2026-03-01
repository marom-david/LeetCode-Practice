class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        i = 0
        while i < len(nums):
            x = target - nums[i]
            if x in dict:
                return [i , dict[x]]
            dict[nums[i]] = i
            i = i +1
                
        