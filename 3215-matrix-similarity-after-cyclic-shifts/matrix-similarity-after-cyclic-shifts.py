class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        R = len(mat)
        C = len(mat[0])
        mat2 = [[None] * C for _ in range(R)]
        for x in range(R):
            for y in range(C):
                if x % 2 == 0:
                    mat2[x][(y - k) % C] = mat[x][y]
                else:
                    mat2[x][(y + k) % C] = mat[x][y]
            for y in range(C):
                if mat2[x][y] != mat[x][y]:
                    return False
        return True