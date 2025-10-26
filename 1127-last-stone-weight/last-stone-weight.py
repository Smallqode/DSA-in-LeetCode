class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)
            if second > first:
                heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])