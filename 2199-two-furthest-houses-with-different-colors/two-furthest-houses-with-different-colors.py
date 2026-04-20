class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)
        best = 0
        for i in range(N):
            for j in range(i + 1, N):
                if colors[i] != colors[j]:
                    best = max(best, abs(j - i))
        return best