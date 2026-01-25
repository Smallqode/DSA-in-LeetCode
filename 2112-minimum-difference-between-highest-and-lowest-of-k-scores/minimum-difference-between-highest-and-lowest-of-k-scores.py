class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = 10 ** 20
        best = INF
        nums.sort()
        for i in range(N - k + 1):
            best = min(best, nums[i + k - 1] - nums[i])
        return best