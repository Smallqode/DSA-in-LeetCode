class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []
        for index, x in enumerate(nums):
            if x == target:
                ans.append(index)
        return ans