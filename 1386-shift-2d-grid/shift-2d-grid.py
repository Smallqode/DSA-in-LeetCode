class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0])
        k %= (R * C)
        new_grid = [[None] * C for _ in range(R)]
        for x in range(R):
            for y in range(C):
                index = x * C + y
                new_index = (index + k) % (R * C)
                nx, ny = new_index // C, new_index % C
                new_grid[nx][ny] = grid[x][y]
        return new_grid