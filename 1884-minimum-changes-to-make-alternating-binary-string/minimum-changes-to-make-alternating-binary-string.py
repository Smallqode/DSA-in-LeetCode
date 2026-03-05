class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)
        best = N
        for start in (0, 1):
            count = 0
            for i in range(N):
                if int(s[i]) != (start + i) % 2:
                    count += 1
            best = min(best, count)
        return best