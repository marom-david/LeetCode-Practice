from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        queue = deque()
        count = 0
        row = len(grid)
        col = len(grid[0])
        mins = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    count += 1

        while queue and count > 0:
            mins += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    count -= 1
                    queue.append((r-1,c))
                    grid[r-1][c] = 2
                if r + 1 < row and grid[r+1][c] == 1:
                    count -= 1
                    queue.append((r+1,c))
                    grid[r+1][c] = 2
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    count -= 1
                    queue.append((r,c-1))
                    grid[r][c-1] = 2
                if c + 1 < col and grid[r][c+1] == 1:
                    count -= 1
                    queue.append((r,c+1))
                    grid[r][c+1] = 2
            
        return mins if count == 0 else -1