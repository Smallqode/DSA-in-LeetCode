class Solution:
    def minMoves(self, nums: List[int]) -> int:
        N = len(nums)
        total = 0
        mx = max(nums)
        for x in nums:
            total += mx - x
        return total