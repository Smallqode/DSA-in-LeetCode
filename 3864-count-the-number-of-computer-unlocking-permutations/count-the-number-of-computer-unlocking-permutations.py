class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        N = len(complexity)
        MOD = 10**9 + 7
        for i in range(1, N):
            if complexity[0] >= complexity[i]:
                return 0
        f = 1
        for i in range(1, N):
            f *= i
            f %= MOD
        return f