import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        brute force:
        list of length len(nums) + 1. index used for counts 
        to get the counts i can use another hm
        hm = {1: 1, 2: 2, 3: 3}
        '''
        count = {}
        result = []
        #heapq.heapify(nums)
        newArr = []
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for key in count:
            newArr.append((count[key] * -1, key))
        heapq.heapify(newArr)
        for i in range(k):
            result.append(heapq.heappop(newArr)[1])
        return result

        '''



        counts = [None] * (len(nums) + 1)
        hm = {}
        result = []
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        for num in hm:
            
            if counts[hm[num]] is None:
                counts[hm[num]] = [num]
            else:
                counts[hm[num]].append(num)

            
            try:
                counts[hm[num]].append(num)
            except:
                counts[hm[num]] = [num]
        count = 0
        for i in range(len(counts) - 1, 0, -1):
            if counts[i] is not None:
                for num in counts[i]:
                    result.append(num)
                    count += 1
            if count == k:
                return result
        return result
        '''