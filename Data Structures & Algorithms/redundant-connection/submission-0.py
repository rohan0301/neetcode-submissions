class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        connection = when theres n edges for n nodes
        given edge = [a,b], redundent connection happens when find(a) == find(b)
        where they both have the same parent
        '''
        edgeLen = len(edges)
        parent = [i for i in range(edgeLen + 1)]
        size = [1] * (edgeLen + 1)

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(p1, p2):
            pf1, pf2 = find(p1), find(p2)
            if pf1 == pf2:
                return [p1,p2]

            if size[pf1] < size[pf2]:
                pf1,pf2 = pf2,pf1
            parent[pf1] = parent[pf2]
            size[pf1] += size[pf2]
        
        for a,b in edges:
            result = union(a,b)
            if result:
                return result
        return []


        