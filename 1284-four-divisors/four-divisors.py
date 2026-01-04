class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def d(x):
            r = 2
            t = 1 + x
            i = 2
            while i * i <= x:
                if x % i == 0:
                    r += 2
                    t += i
                    t += x // i
                    if i * i == x:
                        r -= 1
                        t -= i
                i += 1
            return (r, t)
        total = 0
        for x in nums:
            r, t = d(x)
            if r == 4:
                total += t
        return total