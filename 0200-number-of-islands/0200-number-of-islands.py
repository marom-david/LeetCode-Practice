class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        islands = 0
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    islands += 1
                    self.dfs(grid, r, c)
        
        return islands

    def dfs(self, grid, r, c):
        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] != '1':
            return
        grid[r][c] = '0'

        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r - 1, c)