class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        max_len = 0
        
        for n in nums:
            curr_len = 1
            curr_num = n
            if curr_num-1 not in nums_set:
                while curr_num+1 in nums_set:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)

        return max_len
        