class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        count = 0
        depth = 0
        for c in s:
            if c == "(":
                depth += 1
            else:
                depth -= 1
            if depth < 0:
                depth = 0
                count += 1
        return count + depth