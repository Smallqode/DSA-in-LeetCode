class Solution:
    def judgeCircle(self, moves: str) -> bool:
        f = Counter(moves)
        return f["L"] == f["R"] and f["U"] == f["D"]