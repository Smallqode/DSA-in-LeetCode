class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0
        left_total = 0
        for i in range(len(nums) - 1):
            left_total += nums[i]
            total -= nums[i]
            if (total - left_total) % 2 == 0:
                count += 1
        return count