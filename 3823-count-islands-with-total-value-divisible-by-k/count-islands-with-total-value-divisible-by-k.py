class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        R = len(grid)
        C = len(grid[0])
        directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]
        def f(x, y):
            total = grid[x][y]
            grid[x][y] = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx <R and 0 <= ny < C) and grid[nx][ny] > 0:
                    total += f(nx, ny)
            return total
        count = 0
        for x in range(R):
            for y in range(C):
                if grid[x][y] > 0:
                    if f(x, y) % k == 0:
                        count += 1
        return count