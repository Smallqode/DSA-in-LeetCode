class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        ans = []
        for x, y in zip(nums, nums[1:]):
            for i in range(x + 1, y):
                ans.append(i)
        return ans