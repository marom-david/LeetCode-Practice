class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix[0])
        l = 0
        r = len(matrix)*len(matrix[0]) - 1
        index = (l+r)//2

        while l <= r:
            index = (l+r)//2
            col = index//n
            row = index%n
            if matrix[col][row] == target:
                return True
            if matrix[col][row] > target:
                r = index - 1
            if matrix[col][row] < target:
                l = index + 1

        return False
