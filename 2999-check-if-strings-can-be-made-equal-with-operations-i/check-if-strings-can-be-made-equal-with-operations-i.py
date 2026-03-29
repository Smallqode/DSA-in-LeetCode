class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def get_f(s):
            parity = [Counter(), Counter()]
            for i in range(len(s)):
                parity[i % 2][s[i]] += 1
            return parity
        return get_f(s1) == get_f(s2)