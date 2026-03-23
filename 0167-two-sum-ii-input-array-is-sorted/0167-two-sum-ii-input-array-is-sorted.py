class Solution(object):
    def twoSum(self, numbers, target):
        right = len(numbers) - 1
        left = 0

        while numbers[right] + numbers[left] != target:               
            if numbers[right] + numbers[left] > target:
                right -= 1
            else: 
                left += 1

        return [left + 1,right + 1]