import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            t1 = heapq.heappop(stones)
            t2 = heapq.heappop(stones)
            t1 *= -1
            t2 *= -1
            if t1 > t2:
                t1 = t1 - t2
                heapq.heappush(stones, -t1)
        if len(stones) == 1:
            return stones[0] * -1
        return 0
