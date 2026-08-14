class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        best = 0
        for start in range(n):
            f = Counter()
            for end in range(start, n):
                f[s[end]] += 1
                if f[s[end]] > 2:
                    break
                best = max(best, end - start + 1)
        return best