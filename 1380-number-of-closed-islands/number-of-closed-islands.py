class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]
        def good(x, y):
            grid[x][y] = 2
            allgood = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx <R and 0 <= ny < C):
                    allgood = False
                elif grid[nx][ny] == 0:
                    if not good(nx, ny):
                        allgood = False
            return allgood
        count = 0
        for x in range(R):
            for y in range(C):
                if grid[x][y] == 0:
                    if good(x, y):
                        count += 1
        return count