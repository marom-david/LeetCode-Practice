class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix[0])
        l = 0
        r = len(matrix)*len(matrix[0]) - 1

        while l <= r:
            index = (l+r)//2
            col = index%n
            row = index//n 
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = index + 1
            elif matrix[row][col] > target:
                r = index - 1
        
        return False