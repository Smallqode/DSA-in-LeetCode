class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right, extra = 0, 0, 0
        for x in moves:
            if x == 'L':
                left += 1
            elif x == 'R':
                right += 1
            else:
                extra += 1
        return max(left, right) - min(left, right) + extra