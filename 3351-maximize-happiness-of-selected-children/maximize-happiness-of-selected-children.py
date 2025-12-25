class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        N = len(happiness)
        happiness.sort(reverse=True)
        total = 0
        for i in range(k):
            total += max(0, happiness[i] - i)
        return total