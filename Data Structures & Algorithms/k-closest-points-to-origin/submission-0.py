from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDist(a,b):
            return sqrt((a)**2 + (b)**2)
        
        arr = []
        for x,y in points:
            heapq.heappush(arr, (calcDist(x,y), (x,y)))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr)[1])
        return res