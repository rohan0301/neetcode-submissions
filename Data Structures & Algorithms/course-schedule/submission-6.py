class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        goodNodes = set()
        for a,b in prerequisites:
            if b not in adj:
                adj[b] = []
            adj[b].append(a)
        def dfs(node, path):
            for nxt in adj[node]:
                if nxt in path:
                    return False
                if nxt in goodNodes:
                    continue
                path.append(nxt)
                result = dfs(nxt, path)
                path.pop()
                if result == False:
                    return False
                else:
                    goodNodes.add(nxt)
            return True
        for course in range(numCourses):
            if dfs(course, []) == False:
                return False
        return True
