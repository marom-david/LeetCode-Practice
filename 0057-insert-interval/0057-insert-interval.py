class Solution(object):
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        result = []
        count = 0

        while count < len(intervals) and intervals[count][1] < newInterval[0]:
            result.append(intervals[count])
            count += 1
        
        while count < len(intervals) and intervals[count][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[count][0])
            newInterval[1] = max(newInterval[1], intervals[count][1])
            count += 1
        
        result.append(newInterval)

        while count < len(intervals):
            result.append(intervals[count])
            count += 1

        return result
        