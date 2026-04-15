class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in  words:
            return -1
        best = 10 ** 20
        N = len(words)
        for i in range(N):
            if target == words[i]:
                best = min(best , abs(startIndex - i), abs(startIndex + N - i), abs(startIndex - (i + N)))
        return best