from collections import deque, defaultdict
import heapq
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
        for s, e, time in times:
            adj[s].append((e,time))
        dist = {k: 0}
        q = [(0,k)]
        while q:
            d, node = heapq.heappop(q)
            if d < dist.get(node, float('inf')):
                continue
            for nxt, t in adj[node]:
                newDist = d + t
                if newDist < dist.get(nxt, float('inf')):
                    dist[nxt] = newDist
                    heapq.heappush(q, (newDist, nxt))
        maxVal = float('-inf')
        if len(dist) != n:
            return -1
        for key in dist:
            if dist[key] > maxVal:
                maxVal = dist[key]
        return maxVal

