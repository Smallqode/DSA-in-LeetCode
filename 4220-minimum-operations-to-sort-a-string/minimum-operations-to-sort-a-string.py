class Solution:
    def minOperations(self, s: str) -> int:
        T = "".join(sorted(s))
        N = len(s)
        if N == 2:
            if s[0] <= s[1]:
                return 0
            return -1
        if s == T:
            return 0
        r = s
        if min(r) == r[0] or max(r) == r[-1]:
            return 1
        r = r[0] + "".join(sorted(r[1:]))
        r = "".join(sorted(r[:-1])) + r[-1]
        if r == T:
            return 2
        r = s
        r = "".join(sorted(r[:-1])) + r[-1]
        r = r[0] + "".join(sorted(r[1:]))
        if r == T:
            return 2
        return 3