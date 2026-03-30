import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        max_heap = []

        for s in stones:
            heapq.heappush(max_heap, -s)
        
        while len(max_heap) > 1:
            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap)
            if val1 == val2:
                pass
            elif val1 > val2:
                heapq.heappush(max_heap, -(val1-val2))
            elif val1 < val2:
                heapq.heappush(max_heap, -(val2-val1))
            
        return -max_heap[0] if max_heap else 0