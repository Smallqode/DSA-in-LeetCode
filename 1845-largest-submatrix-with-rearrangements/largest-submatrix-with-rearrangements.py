class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        best = 0
        streak = [0] * C
        for x in range(R):
            for y in range(C):
                if matrix[x][y] == 1:
                    streak[y] += 1
                else:
                    streak[y] = 0
            cells = list(sorted(streak, reverse=True))
            for index, v in enumerate(cells, start=1):
                best = max(best, index * v)
        return best