class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            index = (l+r)//2
            if nums[index] == target:
                return index
            if nums[l] <= nums[index]:
                if nums[l] <= target < nums[index]:
                    r = index - 1
                else:
                    l = index + 1
            else:
                if nums[index] < target <= nums[r]:
                    l = index + 1
                else:
                    r = index - 1

        return -1