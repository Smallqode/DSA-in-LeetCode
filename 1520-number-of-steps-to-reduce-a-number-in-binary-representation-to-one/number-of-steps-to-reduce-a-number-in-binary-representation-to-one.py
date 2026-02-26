class Solution:
    def numSteps(self, s: str) -> int:
        N = len(s)
        carry = 0
        count = 0
        for i in range(N - 1, 0, -1):
            digit = int(s[i])
            digit += carry
            carry = digit // 2
            if digit % 2 == 1:
                count += 1
                carry += 1
            count += 1
        if carry > 0:
            count += 1
        return count