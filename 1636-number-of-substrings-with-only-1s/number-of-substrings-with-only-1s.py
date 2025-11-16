class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        consec = 0
        for c in s:
            if c == "1":
                consec += 1
                res = (res + consec) % MOD
            else:
                consec = 0
        return res