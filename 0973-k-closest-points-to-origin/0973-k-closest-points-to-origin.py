import heapq, math

class Solution(object):
    def kClosest(self, points, k):
        max_heap = []

        for p in points:
            dis = p[0]*p[0] + p[1]*p[1]
            entry = (-dis, p)
            if len(max_heap) < k:
                heapq.heappush(max_heap, entry)
            elif -dis > max_heap[0][0]:
                heapq.heapreplace(max_heap, entry)

        return [item[1] for item in max_heap]