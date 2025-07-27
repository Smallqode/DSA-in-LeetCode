class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i, n in count.items():
            if n > len(nums) // 2:
                return i