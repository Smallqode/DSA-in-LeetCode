class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        f = Counter(word)
        count = 0
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower = 'abcdefghijklmnopqrstuvwxyz'
        for C,c in zip(upper, lower):
            if f[C] > 0 and f[c] > 0:
                count += 1
        return count