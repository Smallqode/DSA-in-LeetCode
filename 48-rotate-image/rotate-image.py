class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        N2 = (N + 1) // 2
        N2odd = N // 2
        for x in range(N2):
            for y in range(N2odd):
                current = matrix[x][y]
                matrix[x][y] = matrix[N - y - 1][x]
                matrix[N - y - 1][x] = matrix[N - x - 1][N - y - 1]
                matrix[N - x - 1][N - y - 1] = matrix[y][N - x - 1]
                matrix[y][N - x - 1] = current
                