class Solution:
    def minElement(self, nums: List[int]) -> int:
        r = []
        for i in nums:
            r.append(sum(int(x) for x in str(i)))
        return min(r)