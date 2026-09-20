class Solution:
    def reverseDegree(self, s: str) -> int:
        prdt = 0
        for i in range(len(s)):
            indx = abs(ord(s[i]) - ord('z')) + 1
            prdt += indx * (i + 1)
        return prdt