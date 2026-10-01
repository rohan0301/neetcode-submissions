from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        currArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    grid[i][j] = 0
                    currArea = 1
                while queue:
                    curr = queue.popleft()
                    x, y = curr[0], curr[1]
                    if x > 0 and grid[x - 1][y] == 1:
                        currArea += 1
                        grid[x-1][y] = 0
                        queue.append((x-1,y))
                    if y > 0 and grid[x][y - 1] == 1:
                        currArea += 1
                        grid[x][y-1] = 0
                        queue.append((x,y-1))
                    if x < n - 1 and grid[x + 1][y] == 1:
                        currArea += 1
                        grid[x+1][y] = 0
                        queue.append((x+1,y))
                    if y < m - 1 and grid[x][y + 1] == 1:
                        currArea += 1
                        grid[x][y+1] = 0
                        queue.append((x,y+1))
                if currArea > maxArea: 
                    maxArea = currArea
        return maxArea

