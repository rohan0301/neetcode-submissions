class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 0
        if digits[0] + 1 == 10:
            carry = 1
            digits[0] = 0
        else:
            digits[0] += 1
        for i in range(1, len(digits)):
            if digits[i] + carry == 10:
                carry = 1
                digits[i] = 0
            else:
                digits[i] = digits[i] + carry
                carry = 0
        if digits[-1] == 0:
            digits[-1] = 0
            digits.append(1)
        digits.reverse()
        return digits