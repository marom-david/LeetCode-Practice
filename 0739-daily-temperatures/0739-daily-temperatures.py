class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for t in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[t]:
                index = stack.pop()
                result[index] = t - index
            stack.append(t)

        return result
        