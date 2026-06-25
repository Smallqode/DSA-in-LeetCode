class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = 0
        for start in range(n):
            count = 0
            for end in range(start, n):
                if nums[end] == target:
                    count += 1
                if count * 2 > (end - start + 1):
                    total += 1
        return total