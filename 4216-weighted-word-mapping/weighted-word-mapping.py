class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def get_sum(word):
            total = 0
            for c in word:
                total += weights[ord(c) - ord('a')]
            return total
        def f(word):
            total = get_sum(word) % 26
            return chr(ord('a') + 26 - total - 1)
        ans = []
        for word in words:
            ans.append(f(word))
        return "".join(ans)