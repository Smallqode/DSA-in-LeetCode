class Solution:
    def climbStairs(self, N: int, costs: List[int]) -> int:
        INF = 10 ** 20
        @cache
        def f(index):
            if index >= N:
                return 0
            best = INF
            for d in range(1, 4):
                if index + d <= N:
                    best = min(best, f(index + d) + costs[index + d - 1] + d * d)
            return best
        return f(0)