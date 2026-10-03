class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def getAllDigits(n):
            lst = []
            while n > 0:
                lst.append(n%10)
                n = n//10
            
            lst.reverse()
            return lst
        newn = n
        while newn != 1:
            lst = getAllDigits(newn)
            for i in range(len(lst)):
                lst[i] = lst[i] * lst[i]
            newn = sum(lst)
            print(newn)
            if newn in seen:
                return False
            else:
                seen.add(newn)
        return True


