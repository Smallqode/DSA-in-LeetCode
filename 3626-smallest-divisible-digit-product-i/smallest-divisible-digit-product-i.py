class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def p(x):
            current = 1
            while x > 0:
                current *= x % 10
                x //= 10
            return current
        while p(n) % t != 0:
            n += 1
        return n