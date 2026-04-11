class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        INF = 10 ** 20
        f = defaultdict(list)
        for index, x in enumerate(nums):
            f[x].append(index)
        best = INF
        for key in f.keys():
            L = f[key]
            for i, j, k in zip(L, L[1:], L[2:]):
                best = min(best, abs(i - j) + abs(j - k) + abs(k - i))
        if best >= INF:
            return -1
        return best