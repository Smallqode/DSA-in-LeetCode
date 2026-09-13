class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        r = len(img1)
        c = len(img1[0])
        best = 0
        for dx in range(- r + 1, r):
            for dy in range(- c + 1, c):
                overlaps = 0
                for x in range(r):
                    nx = x + dx
                    if 0 <= nx < r:
                        for y in range(c):
                            ny = y + dy
                            if 0 <= ny < c and img1[x][y] + img2[x + dx][y + dy] == 2:
                                overlaps += 1
                best = max(best, overlaps)
        return best