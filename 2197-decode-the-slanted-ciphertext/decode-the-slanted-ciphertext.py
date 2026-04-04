class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        N = len(encodedText)
        assert(N % rows == 0)
        cols = N // rows
        matrix = []
        for i in range(rows):
            matrix.append(encodedText[i * cols:(i + 1) * cols])
        ans = []
        for i in range(cols):
            for j in range(rows):
                if i + j < cols:
                    ans.append(matrix[j][i + j])
        return "".join(ans).rstrip(" ")