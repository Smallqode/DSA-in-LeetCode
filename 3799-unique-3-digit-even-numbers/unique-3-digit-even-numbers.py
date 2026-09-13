class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        s = set()
        for k in range(n):
            if digits[k] % 2 == 0:
                for i in range(n):
                    if i != k and digits[i] != 0:
                        for j in range(n):
                            if i != j and j != k:
                                s.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return len(s)