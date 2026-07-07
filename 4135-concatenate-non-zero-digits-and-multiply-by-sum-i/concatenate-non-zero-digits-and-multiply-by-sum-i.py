class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        s = 0
        for i in str(n):
            if i != '0':
                x += i
        if not x:
            return 0
        for j in x:
            s += int(j)
        return s * int(x)