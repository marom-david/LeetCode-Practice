class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat
        
        res = [[0]* c for _ in range(r)]

        for i in range(m*n):
            res[i//c][i%c] = mat[i//n][i%n]
        
        return res
        