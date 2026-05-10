class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        N = len(nums)
        INF = 10 ** 20
        @cache
        def f(index):
            if index == N - 1:
                return 0
            best = -INF
            for j in range(index + 1, N):
                if abs(nums[j] - nums[index]) <= target:
                    best = max(best, f(j) + 1)
            return best
        r = f(0)
        if r <= -1:
            return -1
        return r