class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def eq(a, b):
            N = len(a)
            for i in range(N):
                for j in range(N):
                    if mat[i][j] != target[i][j]:
                        return False
            return True
        def rot(a):
            N = len(a)
            r = [[None] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    r[i][j] = a[j][N - i - 1]
            return r
        for _ in range(4):
            if eq(mat, target):
                return True
            mat = rot(mat)
        return False