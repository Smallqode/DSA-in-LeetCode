class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        INF = 10 ** 20
        lookup = {}
        best = INF
        def reverse(x):
            return int(str(x)[::-1])
        for index, x in enumerate(nums):
            if x in lookup:
                best = min(best, index - lookup[x])
            lookup[reverse(x)] = index
        if best >= INF:
            return -1
        return best