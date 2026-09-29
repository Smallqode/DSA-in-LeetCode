class Solution:
    def maxDepth(self, s: str) -> int:
        best = 0
        depth = 0
        for c in s:
            if c == "(":
                depth += 1
                best = max(best, depth)
            elif c == ")":
                depth -= 1
        return best