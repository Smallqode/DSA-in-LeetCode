class Solution:
    def maxProduct(self, n: int) -> int:
        def get_digit(x):
            d = []
            while x > 0:
                d.append(x % 10)
                x //= 10
            return d
        digits = list(sorted(get_digit(n)))
        return digits[-1] * digits[-2]