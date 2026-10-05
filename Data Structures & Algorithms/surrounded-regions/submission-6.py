from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        loop through each cell until we reach 'O' thats not at the edge. if its not, append to queue and bfs making sure nothings on the edge. if it is then fade else keep track of all coordinates of this bfs and then go back and convert all of them to 'x'
        if an edge, bfs through the rest of the region 

        '''
        n = len(board)
        m = len(board[0])
        q = deque()
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if board[i][j] == 'O':
                        q.append((i,j))
                        while q:
                            curr = q.popleft()
                            row = curr[0]
                            col = curr[1]
                            board[row][col] = 'T'
                            for r,c in d:
                                nrow = row + r
                                ncol = col + c
                                if 0 <= nrow < n and 0 <= ncol < m and board[nrow][ncol] == 'O':
                                    q.append((nrow,ncol))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'












        '''
        q = deque()
        currList = []
        seen = set()
        d = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(1,n-1):
            for j in range(1, m-1):
                if board[i][j] == 'O' and (i,j) not in seen:
                    currSeen = set()
                    currSeen.add((i,j))
                    q.append((i,j))
                    edgeFound = False
                    while q:
                        curr = q.popleft()
                        row = curr[0]
                        col = curr[1]
                        for r,c in d:
                            nrow = row + r
                            ncol = col + c
                            if 0 <= nrow < n and 0 <= ncol < m and board[nrow][ncol] == 'O' and (nrow,ncol) not in currSeen:
                                if (nrow == 0 or ncol == 0 or nrow == n-1 or ncol == m-1) or (nrow,ncol) in seen:
                                    edgeFound = True
                                currSeen.add((nrow,ncol))
                                q.append((nrow,ncol))
                    if edgeFound:
                        for coords in currSeen:
                            seen.add(coords)
                    else:
                        for coords in currSeen:
                            board[coords[0]][coords[1]] = 'X'
        '''

