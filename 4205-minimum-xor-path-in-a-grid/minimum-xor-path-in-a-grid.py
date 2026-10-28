class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        INF = 10 ** 20
        R = len(grid)
        C = len(grid[0])
        q = deque()
        s = [[set() for _ in range(C)] for _ in range(R)]
        def enqueue(x, y, xor):
            if xor in s[x][y]:
                return
            q.append((x, y, xor))
            s[x][y].add(xor)
        directions = [(1, 0), (0, 1)]
        enqueue(0, 0, grid[0][0])
        best = INF
        while len(q) > 0:
            x, y, xor = q.popleft()
            if x == R - 1 and y == C - 1:
                best = min(best, xor)
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    nxor = xor ^ grid[nx][ny]
                    if nxor in s[nx][ny]:
                        continue
                    q.append((nx, ny, nxor))
                    s[nx][ny].add(nxor)
        return best