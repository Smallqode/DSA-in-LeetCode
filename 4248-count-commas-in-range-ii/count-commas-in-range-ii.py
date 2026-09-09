class Solution:
    def countCommas(self, n: int) -> int:
        curr = 1000
        count = 0
        while n >= curr:
            count += n - (curr - 1)
            curr *= 1000
        return count