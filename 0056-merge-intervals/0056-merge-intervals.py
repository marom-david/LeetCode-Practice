class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        start = 0
        end = 0 
        merged = [intervals[0]]
        
        for i in intervals:
            if i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)
            
        return merged