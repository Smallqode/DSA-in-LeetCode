class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        INF = (1 << 32) - 1
        best = INF

        for i, x in enumerate(nums):
            if i != x:
                best &= x
        if best == INF:
            return 0
        return best