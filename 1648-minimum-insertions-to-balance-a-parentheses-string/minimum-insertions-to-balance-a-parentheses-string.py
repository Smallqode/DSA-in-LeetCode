class Solution:
    def minInsertions(self, s: str) -> int:
        moves = 0
        depth = 0
        for c in s:
            if c == "(":
                if depth % 2 == 1:
                    depth -= 1
                    moves += 1
                depth += 2
            else:
                depth -= 1
                if depth < 0:
                    depth += 2
                    moves += 1
        return moves + depth