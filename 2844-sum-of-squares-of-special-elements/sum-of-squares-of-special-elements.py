class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        for i in range(N):
            if N % (i + 1) == 0:
                res += nums[i] * nums[i]
        return res