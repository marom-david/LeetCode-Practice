class Solution(object):
    def topKFrequent(self, nums, k):
        num_sum = {}

        for num in nums:
            if num in num_sum:
                num_sum[num] += 1
            else:
                num_sum[num] = 1

        sorted_items = sorted(num_sum.items(), key=lambda x:x[1], reverse = True)
        return [sorted_items[i][0] for i in range(k)]

        