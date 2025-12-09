class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = 10**9 + 7
        left = Counter()
        right = Counter(nums)
        count = 0
        for j in range(N):
            right[nums[j]] -= 1            
            count += left[nums[j] * 2] * right[nums[j] * 2]
            count %= MOD
            left[nums[j]] += 1
        return count % MOD