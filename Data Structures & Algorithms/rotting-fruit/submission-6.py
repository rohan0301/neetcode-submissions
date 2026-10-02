from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        one pass through the grid and identify every rotton fruit
        if rotten, append it to queue
        start bfs and once bfs ends count amt of levels
        '''
        n = len(grid)
        m = len(grid[0])
        q = deque()
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        nExists = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
        count = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for r,c in d:
                    nr,nc = curr[0] + r, curr[1] + c
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 0
                        #nExists = True
            if q:
                count += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return count

