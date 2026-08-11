class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)
        total = 0
        for x, y in zip(nums, nums[1:]):
            total += x
            if y != x + 1:
                while total in s:
                    total += 1
                return total
        else:
            total += nums[-1]
            while total in s:
                total += 1
            return total