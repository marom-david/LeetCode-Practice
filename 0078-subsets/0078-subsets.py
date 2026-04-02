class Solution(object):
    def subsets(self, nums):
        result = []

        def backtrack(start_index, current_path):
            result.append(list(current_path))
            
            for i in range(start_index, len(nums)):
                current_path.append(nums[i])
                backtrack(i+1, current_path)
                current_path.pop()
            
        backtrack(0, [])
        return result

        