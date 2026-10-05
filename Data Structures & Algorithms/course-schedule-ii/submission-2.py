from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        result = []
        degreeMap = {i: 0 for i in range(numCourses)}
        for course in adj:
            for courses in adj[course]:
                degreeMap[courses] += 1
        q = deque()
        for course in degreeMap:
            if degreeMap[course] == 0:
                q.append(course)
        while q:
            curr = q.popleft()
            result.append(curr)
            for courses in adj[curr]:
                degreeMap[courses] -= 1
                if degreeMap[courses] == 0:
                    q.append(courses)
        return result if len(result) == numCourses else []
