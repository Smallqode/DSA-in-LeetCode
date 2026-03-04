class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])
        row = [0] * R
        col = [0] * C
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        count = 0
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    count += 1
        return count