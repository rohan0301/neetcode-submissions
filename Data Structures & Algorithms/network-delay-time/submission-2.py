from collections import deque, defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        basically keep going until list of unvisited nodes is empty
        keep 2 maps of one containing previous node and one containing shortest distance to that node
        visited/unvisited can both be sets
        to visit each node we use bfs

        pop from queue:
        check distance:
            shortest[k] + time
        '''
        adj = defaultdict(list)
        visited = set()
        unvisited = set()
        prevNode = {i: None for i in range(1,n + 1)}
        shortest = {i: float('inf') for i in range(1, n+1)}
        for s, e, time in times:
            if s not in unvisited:
                unvisited.add(s)
            if e not in unvisited:
                unvisited.add(e)
            adj[s].append((e,time))
        q = deque()
        q.append(k)
        shortest[k] = 0
        while q:
            curr = q.popleft()
            for nxt, time in adj[curr]:
                if shortest[nxt] > (time + shortest[curr]):
                    shortest[nxt] = (time + shortest[curr])
                    prevNode[nxt] = curr
                    q.append(nxt)
            if curr not in visited:
                visited.add(curr)
            if curr in unvisited:
                unvisited.remove(curr)
        if len(unvisited) != 0:
            return -1
        count = float('-inf')
        for key in shortest:
            if shortest[key] > count:
                count = shortest[key]
        if count == float('inf'):
            count = -1
        return count

