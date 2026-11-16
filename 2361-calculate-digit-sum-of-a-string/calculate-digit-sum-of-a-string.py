class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            r = []
            for i in range(len(s)):
                if i % k == 0:
                    r.append(0)
                r[-1] += int(s[i])
            s = "".join(str(x) for x in r)
        return s