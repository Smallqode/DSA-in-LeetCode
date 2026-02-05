class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        for i in range(N):
            ans.append(nums[(i + nums[i]) % N])
        return ans