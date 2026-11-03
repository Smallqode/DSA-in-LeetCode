class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        N = len(nums)
        nums.sort()
        target = nums[N // 2]
        total = 0
        for x in nums:
            total += abs(x - target)
        return total