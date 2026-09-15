class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        def overlap(s1, e1, s2, e2):
            return min(e1, e2) - max(s1, s2) > 0
        return overlap(ax1, ax2, bx1, bx2) and overlap(ay1, ay2, by1, by2)