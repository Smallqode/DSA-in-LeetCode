class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        INF = 10 ** 20
        def increasing(arr):
            streak = 0
            best = 0
            prev = -INF
            for x in arr:
                if x > prev:
                    streak += 1
                else:
                    streak = 1
                best = max(best, streak)
                prev = x
            return best
        return max(increasing(nums), increasing(list(-x for x in nums)))