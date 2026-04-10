class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        INF = 10 ** 20
        best = INF
        N = len(nums)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i != j and j != k and k != i:
                        if nums[i] == nums[j] == nums[k]:
                            best = min(best, abs(i - j) + abs(j - k) + abs(k - i))
        if best == INF:
            return -1
        return best