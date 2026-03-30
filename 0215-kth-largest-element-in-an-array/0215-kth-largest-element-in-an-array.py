import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = []
        
        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            elif n > min_heap[0]:
                heapq.heappush(min_heap, n)
                heapq.heappop(min_heap)
        
        return min_heap[0]
        