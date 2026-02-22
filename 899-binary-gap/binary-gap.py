class Solution:
    def binaryGap(self, N: int) -> int:
        B = 30
        pos = []
        for i in range(B):
            if (N & (1 << i)) > 0:
                pos.append(i)
        best = 0
        for j in range(len(pos) - 1):
            best = max(best, pos[j + 1] - pos[j])
        return best