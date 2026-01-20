class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def f(x):
            for i in range(1, x + 1):
                if i | (i + 1) == x:
                    return i
            return -1
        ans = []
        for x in nums:
            ans.append(f(x))
        return ans