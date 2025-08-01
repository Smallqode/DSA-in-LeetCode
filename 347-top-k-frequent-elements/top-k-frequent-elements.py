class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = []
        for _ in range(k):
            arr.append(max(count, key = count.get))
            count[max(count, key = count.get)] = 0
        return arr