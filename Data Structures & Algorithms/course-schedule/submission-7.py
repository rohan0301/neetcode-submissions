class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
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
        '''
        adj = {i: [] for i in range(numCourses)}
        goodNodes = set()
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        degreeMap = {i: 0 for i in range(numCourses)}
        for key in adj:
            for courses in adj[key]:
                degreeMap[courses] += 1
        q = deque()
        result = []
        for course in degreeMap:
            if degreeMap[course] == 0:
                q.append(course)
        while q:
            curr = q.popleft()
            result.append(curr)
            for nodes in adj[curr]:
                degreeMap[nodes] -= 1
                if degreeMap[nodes] == 0:
                    q.append(nodes)
        return True if len(result) == numCourses else False
