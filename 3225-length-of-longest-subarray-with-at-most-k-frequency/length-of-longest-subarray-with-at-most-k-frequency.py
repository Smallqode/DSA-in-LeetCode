class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = 0
        f = Counter()
        left = 0
        for right in range(n):
            f[nums[right]] += 1
            while f[nums[right]] > k:
                f[nums[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best