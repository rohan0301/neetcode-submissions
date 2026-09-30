class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        zxyzxyz
        left and right intial at 0
        while r < len(s)
            while s[r] not in hm:
                r += 1
                hm[s[r]] = r
            maxNum = r - l
            l = hm[s[r]] + 1
        
        '''
        l = 0
        hm = {}
        maxNum = 0
        lastR = 0
        for r in range(len(s)):
            if s[r] not in hm:
                hm[s[r]] = r
            else:
                maxNum = max(r - l, maxNum)
                l = max(hm[s[r]] + 1, l)
                hm[s[r]] = r
        maxNum = max(len(s) - l, maxNum)
        '''
        while r < len(s):
            while r < len(s) and s[r] not in hm:
                hm[s[r]] = r
                r += 1
            maxNum = max(r - l, maxNum)
            if r < len(s):
                l = hm[s[r]] + 1
                hm[s[r]] = r
                r += 1
                '''
        return maxNum
