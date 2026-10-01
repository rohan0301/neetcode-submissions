class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < len(s) and (s[l] == " " or not s[l].isalnum()):
                l += 1
            while r > 0 and (s[r] == " " or not s[r].isalnum()):
                r -= 1
            if l < r:
                if s[l].upper() != s[r].upper():
                    print(f"l: {s[l]} and r: {s[r]}")
                    return False
            l += 1
            r -= 1
        return True