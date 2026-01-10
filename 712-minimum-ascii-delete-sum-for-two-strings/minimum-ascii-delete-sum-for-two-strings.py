class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N1 = len(s1)
        N2 = len(s2)
        INF = 10**20
        @cache
        def f(index1, index2):
            if index1 == N1 and index2 == N2:
                return 0
            if index1 == N1:
                return f(index1, index2 + 1) + ord(s2[index2])
            if index2 == N2:
                return f(index1 + 1, index2) + ord(s1[index1])
            best = INF
            if s1[index1] == s2[index2]:
                best = min(best, f(index1 + 1, index2 + 1))
            best = min(best, f(index1 + 1, index2) + ord(s1[index1]))
            best = min(best, f(index1, index2 + 1) + ord(s2[index2]))
            return best
        return f(0, 0)