class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        best = 0
        for start in range(N):
            f = Counter()
            mx = 0
            for end in range(start, N):
                f[s[end]] += 1
                mx = max(mx, f[s[end]])
                if mx * len(f) == (end - start + 1):
                    best = max(best, end - start + 1)
        return best