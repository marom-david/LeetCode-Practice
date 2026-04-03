class Solution(object):
    def majorityElement(self, nums):
        appearance = {}

        for i in nums:
            appearance[i] = appearance.get(i, 0) + 1
        
        for num, appear in appearance.items():
            if appear > len(nums)//2:
                return num