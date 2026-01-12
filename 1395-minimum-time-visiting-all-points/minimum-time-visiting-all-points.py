class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        def d(ax, ay, bx, by):
            return max(abs(ax - bx), abs(ay - by))
        for (ax, ay), (bx, by) in zip(points, points[1:]):
            total += d(ax, ay, bx, by)
        return total