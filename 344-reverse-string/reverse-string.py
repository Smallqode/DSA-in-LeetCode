class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(i, j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
        
        i, j = 0, len(s) - 1
        while i < j:
            swap(i, j)
            i += 1
            j -= 1