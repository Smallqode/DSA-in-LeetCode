class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0])
        for dx in range(k//2):
            for dy in range(k):
                grid[x+dx][y+dy], grid[x+(k-dx-1)][y+dy] = grid[x+(k-dx-1)][y+dy], grid[x+dx][y+dy]
        return grid