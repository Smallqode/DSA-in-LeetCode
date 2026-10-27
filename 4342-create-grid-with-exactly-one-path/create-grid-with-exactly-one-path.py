class Solution:
    def createGrid(self, R: int, C: int) -> list[str]:
        grid = [["#"] * C for _ in range(R)]
        for i in range(R):
            grid[i][0] = "."
        for i in range(C):
            grid[R - 1][i] = "."
        ans = []
        for row in grid:
            ans.append("".join(row))
        return ans