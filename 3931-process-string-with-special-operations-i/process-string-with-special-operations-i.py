class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for c in s:
            if c == '*':
                if len(ans) > 0:
                    ans.pop()
            elif c == '#':
                ans += ans
            elif c == '%':
                ans = ans[::-1]
            else:
                ans.append(c)
        return "".join(ans)