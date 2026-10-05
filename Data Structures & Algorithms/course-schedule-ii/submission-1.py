from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        first make sure its acyclic
        '''
        adj = {i: [] for i in range(numCourses)}
        goodNodes = set()
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            '''
        def dfs(node, path):
            for idx in adj[node]:
                if idx in path:
                    return False
                if idx in goodNodes:
                    continue
                path.append(idx)
                result = dfs(idx,path)
                path.pop()
                if result == False:
                    return False
            return True

        for courses in range(numCourses):
            if dfs(courses,[]) == False:
                return []
            '''
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
        return result if len(result) == numCourses else []
            

        