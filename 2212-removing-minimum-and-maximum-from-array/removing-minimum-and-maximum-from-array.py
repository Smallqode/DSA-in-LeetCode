class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        N = len(nums)
        mx = max(nums)
        mn = min(nums)
        mxi = nums.index(mx)
        mni = nums.index(mn)
        left, right = min(mxi, mni), max(mxi, mni)
        return min(right + 1, N - left, (left + 1) + (N - right))