class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        q = collections.deque(sorted(x * x for x in nums))
        total = 0
        while len(q) >= 2:
            total -= q.popleft()
            total += q.pop()
        if len(q) > 0:
            total += q.pop()
        return total