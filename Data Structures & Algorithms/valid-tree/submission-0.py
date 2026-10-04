class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hm = {i: [] for i in range(n)}
        for a,b in edges:
            hm[a].append(b)
            hm[b].append(a)
        seen = set()

        def dfs(node, parent):
            for nxt in hm[node]:
                if nxt == parent:
                    continue
                if nxt in seen:
                    return False
                seen.add(nxt)
                if not dfs(nxt, node):
                    return False
            return True

        result = dfs(0,0)
        if result == False or len(seen) != n -1 :
            return False
        return True