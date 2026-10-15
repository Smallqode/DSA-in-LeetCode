class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        N = len(nums)
        total = 0
        for i in range(N):
            f = set()
            for j in range(i, N):
                f.add(nums[j])
                total += len(f) ** 2
        return total