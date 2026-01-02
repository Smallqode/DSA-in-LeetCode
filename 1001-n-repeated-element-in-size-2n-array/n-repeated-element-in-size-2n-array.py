class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums) // 2
        for num, freq in count.items():
            if freq == n:
                return num