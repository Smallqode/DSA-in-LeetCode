class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        N = len(cost)
        cost.sort(reverse=True)
        total = 0
        for i in range(N):
            if (i % 3) != 2:
                total += cost[i]
        return total