class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        R = len(grid)
        C = len(grid[0])
        total = 0
        for x in range(R):
            for y in range(C):
                total += grid[x][y]
        def can_cut(g):
            R = len(g)
            C = len(g[0])
            prefix = 0
            for x in range(R):
                current = sum(g[x])
                prefix += current
                if total - prefix == prefix:
                    return True
            else:
                return False
        def rot(g):
            R = len(g)
            C = len(g[0])
            r = [[None] * R for _ in range(C)]
            for x in range(R):
                for y in range(C):
                    r[C - y - 1][x] = grid[x][y]
            return r
        r = rot(grid)
        return can_cut(grid) or can_cut(r)