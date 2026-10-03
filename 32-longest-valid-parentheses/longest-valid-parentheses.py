class Solution:
    def longestValidParentheses(self, s: str) -> int:
        seen = {}
        best = 0
        current = 0
        seen[current] = -1
        for index, c in enumerate(s):
            if c == "(":
                current += 1
            else:
                current -= 1
                if current + 1 in seen:
                    del seen[current + 1]
                if current in seen:
                    best = max(best, index - seen[current])
            if current not in seen:
                seen[current] = index
        return best