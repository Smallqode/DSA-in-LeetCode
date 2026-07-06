class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        def inside(a, b):
            return b[0] <= a[0] <= a[1] <= b[1]
        count = 0
        for i in range(N):
            good = True
            for j in range(N):
                if i == j:
                    continue
                if inside(intervals[i], intervals[j]):
                    good = False
                    break
            if good:
                count += 1
        return count