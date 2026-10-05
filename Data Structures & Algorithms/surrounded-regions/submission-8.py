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
                        board[i][j] = 'T'
                        q.append((i,j))
                        while q:
                            curr = q.popleft()
                            
                            for r,c in d:
                                nrow = curr[0] + r
                                ncol = curr[1] + c
                                if 0 <= nrow < n and 0 <= ncol < m and board[nrow][ncol] == 'O':
                                    board[nrow][ncol] = 'T'
                                    q.append((nrow,ncol))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
