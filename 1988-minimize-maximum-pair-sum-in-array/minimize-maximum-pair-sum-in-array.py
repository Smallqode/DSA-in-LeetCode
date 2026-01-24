class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        best = -1
        for i in range(N//2):
            best = max(best, nums[i] + nums[N - i - 1])
        return best