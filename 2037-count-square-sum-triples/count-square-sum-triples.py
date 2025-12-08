class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n+1):
            for b in range(a, n+1):
                c2 = a*a + b*b
                c = int(math.isqrt(c2))
                if c*c == c2 and c <= n:
                    if a == b:
                        ans += 1
                    else:
                        ans += 2
        return ans