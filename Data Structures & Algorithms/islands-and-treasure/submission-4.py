from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        traverse through the graph,. 
        if 214... is found, bfs until treasure is found and use amt of iterations as the count
        if -1 is found, mark -1 on the result array
        if 0 is found, mark 0 on the result array

        '''
        n = len(grid)
        m = len(grid[0])
        #result = [[-1] * n] * m
        d = [(1,0),(-1,0), (0,1), (0,-1)]
        q = deque()
        seen = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
        count = 0
        while q:
            lenq = len(q)
            #seen = set()
            for _ in range(lenq):
                curr = q.popleft()
                seen.add(curr)
                for r,c in d:
                    nr, nc = curr[0] + r, curr[1] + c
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > 0 and (nr,nc) not in seen:
                        currNum = grid[curr[0]][curr[1]]
                        if currNum == 0:
                            grid[nr][nc] = 1
                        else:
                            grid[nr][nc] = currNum + 1
                        q.append((nr,nc))
                        seen.add((nr,nc))
            #count += 1







'''

                if grid[i][j] == 2147483647:
                    queue = deque()
                    seen = set()
                    queue.append((i,j))
                    seen.add((i,j))
                    count = 0
                    tfound = False
                    notFound = False
                    print("here")
                    while queue and not tfound:
                        qlen = len(queue)
                        for _ in range(qlen):
                            curr = queue.popleft()
                            if grid[curr[0]][curr[1]] == 0:
                                tfound = True
                                #print(f"here at {count}")
                                break
                            for r,c in d:
                                nr, nc = curr[0] + r, curr[1] + c
                                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != -1 and (nr,nc) not in seen:
                                    queue.append((nr,nc))
                                    seen.add((nr,nc))
                       #if count > m*n:
                       #    notFound = True
                        if not tfound:
                            count += 1
                    if tfound:
                        grid[i][j] = count
                    '''

