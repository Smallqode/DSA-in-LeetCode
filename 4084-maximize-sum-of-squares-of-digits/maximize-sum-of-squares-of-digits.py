class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        nines = sum // 9
        M = "9" * nines
        if (sum % 9) > 0:
            M += str(sum % 9)
        if len(M) > num:
            return ""
        delta = num - len(M)
        M += "0" * delta
        return M