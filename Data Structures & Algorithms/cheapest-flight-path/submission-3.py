from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        first create adjacency list
        dikstra:
        start at starting node with cost = 0 rest nodes cost is infinity
        dfs to end node keeping track of cost and number of stops
        dfs basecase is:
            end is reached return price
            stops = k (if end is not reached) return None

        '''
        memo = {}
        adj = defaultdict(list)
        for start, end, cost in flights:
            adj[start].append((end,cost))
        
        def dfs(node, stops):
            if (node,stops) in memo:
                return memo[(node, stops)]
            if node == dst:
                return 0
            elif stops > k:
                return float('inf')
            result = float('inf')
            for nxt, price in adj[node]:
                result = min(result, price + dfs(nxt, stops + 1))
            memo[(node,stops)] = result
            return result
        result = dfs(src,0)
        if result == float('inf'):
            return -1
        return result