class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N = len(s)
        for _ in range(N):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False