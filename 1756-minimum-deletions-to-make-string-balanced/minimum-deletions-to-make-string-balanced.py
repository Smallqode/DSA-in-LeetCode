class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        best = N
        b_left = 0
        a_right = s.count("a")
        best = min(best, b_left + a_right)
        for i in range(N):
            if s[i] == 'a':
                a_right -= 1
            else:
                b_left += 1
            best = min(best, b_left + a_right)
        return best