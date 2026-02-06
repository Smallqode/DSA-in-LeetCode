class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        best = 0
        right = 0
        for left in range(N):
            while right < N and nums[right] <= nums[left] * k:
                right += 1
            best = max(best, right - left)
        return N - best