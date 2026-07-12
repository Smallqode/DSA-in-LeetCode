class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = list(set(arr))
        s.sort()
        rank = {}
        for index, x in enumerate(s, 1):
            rank[x] = index
        return list(rank[x] for x in arr)