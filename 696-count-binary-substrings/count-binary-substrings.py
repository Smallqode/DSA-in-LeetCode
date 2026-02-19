class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        streak = 0
        cur = None
        for c in s:
            if cur == c:
                streak += 1
            else:
                if streak > 0:
                    groups.append(streak)
                streak = 1
                cur = c
        else:
            groups.append(streak)
        total = 0
        for x, y in zip(groups, groups[1:]):
            total += min(x, y)
        return total