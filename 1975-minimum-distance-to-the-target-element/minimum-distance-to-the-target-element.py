class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        INF = 10 ** 20
        best = INF
        for i in range(len(nums)):
            if nums[i] == target:
                best = min(best, abs(i - start))
        return best