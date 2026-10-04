class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        count = 0
        hm = {i: [] for i in range(n)}
        '''
        hm = {2: [3, 1], 3: [2, 1], 1: [2,3]}
        '''
        for a,b in edges:
            if a not in hm:
                hm[a] = [b]
            else:
                hm[a].append(b)
            if b not in hm:
                hm[b] = [a]
            else:
                hm[b].append(a)
        
        def dfs(node):
            seen.add(node)
            
            for nodes in hm[node]:
                if nodes not in seen:
                    dfs(nodes)
                
        for node in hm:
            if node not in seen:
                dfs(node)
                count += 1
        return count