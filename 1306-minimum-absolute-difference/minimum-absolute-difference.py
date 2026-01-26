class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        INF = 10**20
        N = len(arr)
        arr.sort()
        best = INF
        ans = []
        for i in range(N - 1):
            x, y = arr[i], arr[i + 1]
            if y -x < best:
                best = y -x
                ans = [[x, y]]
            elif y -x == best:
                ans.append([x, y])
        return ans