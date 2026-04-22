class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def delta(a, b):
            c = 0
            for x, y in zip(a, b):
                if x != y:
                    c += 1
            return c
        ans = []
        for q in queries:
            good = False
            for d in dictionary:
                if delta(q, d) <= 2:
                    good = True
                    break
            if good:
                ans.append(q)
        return ans