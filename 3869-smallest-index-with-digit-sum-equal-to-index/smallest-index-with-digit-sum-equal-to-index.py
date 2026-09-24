class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def dsum(i):
            total = 0
            while i > 0:
                total += i % 10
                i //= 10
            return total
        for i in range(len(nums)):
            if dsum(nums[i]) == i:
                return i
        return -1