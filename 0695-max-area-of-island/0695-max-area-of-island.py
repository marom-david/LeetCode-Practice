class Solution(object):
    def maxAreaOfIsland(self, grid):
        max_area = 0 
        col = len(grid[0])
        row = len(grid)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.dfs(grid, r, c))

        return max_area
        
    def dfs(self, grid, r, c):
        area = 0
        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] != 1:
            return area
        grid[r][c] = 0
        area += 1
        
        area += self.dfs(grid, r + 1, c)
        area += self.dfs(grid, r, c + 1)
        area += self.dfs(grid, r, c - 1)
        area += self.dfs(grid, r - 1, c)
        
        return area