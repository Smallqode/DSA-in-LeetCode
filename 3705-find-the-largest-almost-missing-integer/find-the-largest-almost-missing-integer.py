class Solution:
    def largestInteger(self, nums: List[int], K: int) -> int:
        n = len(nums)
        if n == K:
            f = Counter(nums)
            return max((k for k, v in f.items()), default = -1)
        if K == 1:
            f = Counter(nums)
            return max((k for k, v in f.items() if v == 1), default = -1)
        f = Counter(nums)
        p = []
        if f[nums[0]] == 1:
            p.append(nums[0])
        if f[nums[-1]] == 1:
            p.append(nums[-1])
        return max(p, default = -1)