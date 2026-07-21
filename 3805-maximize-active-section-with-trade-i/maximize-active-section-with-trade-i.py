class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        past = []
        for g, t in groupby(s):
            if g == "0":
                past.append(len(list(t)))
        ones = s.count("1")
        best = ones
        for a, b in zip(past, past[1:]):
            best = max(best, ones + a + b)
        return best