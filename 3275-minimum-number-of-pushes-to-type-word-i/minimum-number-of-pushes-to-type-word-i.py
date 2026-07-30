class Solution:
    def minimumPushes(self, word: str) -> int:
        f = Counter(word)
        cost = 1
        count = 0
        total = 0
        for k, v in sorted(f.items(), key=lambda item:item[1], reverse=True):
            total += v * cost
            count += 1
            if count == 8:
                count = 0
                cost += 1
        return total