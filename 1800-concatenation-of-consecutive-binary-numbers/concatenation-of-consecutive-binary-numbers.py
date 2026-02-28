class Solution:
    def concatenatedBinary(self, N: int) -> int:
        MOD = 10**9 + 7
        cur = 0
        last = 1
        for i in range(1, N + 1):
            if (i & (i - 1)) == 0:
                last *= 2
            cur *= last
            cur += i
            cur %= MOD
        return cur