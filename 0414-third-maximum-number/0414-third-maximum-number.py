class Solution(object):
    def thirdMax(self, nums):
        first_max = second_max = third_max = -float('inf')

        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif first_max > num > second_max:
                third_max = second_max
                second_max = num
            elif second_max > num > third_max:
                third_max = num

        if third_max == -float('inf'):
            return first_max
        else: return third_max
        