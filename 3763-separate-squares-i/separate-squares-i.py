class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        for x, y, L in squares:
            total += L * L
        left = 0
        right = 1e9
        def good(target):
            current = 0
            for x, y, L in squares:
                if y + L <= target:
                    current += L * L
                elif y > target:
                    current += 0
                else:
                    below_length = target - y
                    above_length = y + L - target
                    current += below_length * L
            return current * 2 >= total
        for _ in range(50):
            mid = (left + right) / 2
            if good(mid):
                right = mid
            else:
                left = mid
        return left